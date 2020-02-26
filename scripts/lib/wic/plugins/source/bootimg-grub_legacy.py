#
# SPDX-License-Identifier: GPL-2.0-only
#
# DESCRIPTION
# This implements the 'bootimg-grub_legacy' source plugin class for 'wic'
#
# AUTHORS
# Norbert Kamiński <norbert.kaminski (at) 3mbeb.com>
#

import logging
import os
import shutil

from wic import WicError
from wic.engine import get_custom_config
from wic.pluginbase import SourcePlugin
from wic.misc import (exec_cmd, exec_native_cmd,
                      get_bitbake_var, BOOTDD_EXTRA_SPACE)

logger = logging.getLogger('wic')


class BootimgGrubLegacyPlugin(SourcePlugin):
    """
    Create partition for Grub legacy.
    """

    name = 'bootimg-grub_legacy'

    @classmethod
    def _get_bootimg_dir(cls, bootimg_dir, dirname):
        """
        Check if dirname exists in default bootimg_dir or in STAGING_DIR.
        """
        for result in (bootimg_dir, get_bitbake_var("STAGING_DIR")):
            if os.path.exists("%s/%s" % (result, dirname)):
                return result

        raise WicError("Couldn't find correct bootimg_dir exiting")

    @classmethod
    def do_install_grub_legacy(cls, cr_workdir, native_sysroot):
        """
        Install grub legacy on the boot partition.
        """
        disk_dir = "%s/hdd" % cr_workdir
        grub_legacy_install_cmd = "grub-install %s" % disk_dir
        exec_cmd(grub_legacy_install_cmd, native_sysroot)

    @classmethod
    def do_configure_grub_legacy(cls, hdddir, creator, cr_workdir,
                                 source_params):
        """
        Create grub-legacy config
        """
        # Create config file
        bootloader = creator.ks.bootloader

        grub_conf = ""
        grub_conf += "serial --unit=0 --speed=115200\n"
        grub_conf += "terminal --timeout=%s serial\n" % bootloader.timeout
        grub_conf += "default=boot\n"
        grub_conf += "menuentry 'boot' {\n"

        kernel = "/bzImage"
        rootdev = "/dev/sda"

        grub_conf += "linux %s root=%s rootwait %s\n" \
            % (kernel, rootdev, bootloader.append)

        initrd = source_params.get('initrd')

        if initrd:
            grub_conf += "initrd /%s\n" % initrd

        grub_conf += "}\n"

        logger.debug("Writing grub config %s/hdd/boot/grub/grub.cfg",
                     cr_workdir)
        cfg = open("%s/hdd/boot/grub/grub.cfg" % cr_workdir, "w")
        cfg.write(grub_conf)
        cfg.close()

    @classmethod
    def do_configure_partition(cls, part, source_params, creator, cr_workdir,
                               oe_builddir, bootimg_dir, kernel_dir,
                               native_sysroot):
        """
        Called before do_prepare_partition(), creates loader specific config
        """
        hdddir = "%s/hdd/boot" % cr_workdir
        install_cmd = "install -d %s/grub" % hdddir
        exec_cmd(install_cmd)
        cls.do_configure_grub_legacy(hdddir, creator, cr_workdir, source_params)

    @classmethod
    def do_prepare_partition(cls, part, source_params, creator, cr_workdir,
                             oe_builddir, bootimg_dir, kernel_dir,
                             rootfs_dir, native_sysroot):
        """
        Called to do the actual content population for a partition i.e. it
        'prepares' the partition to be incorporated into the image.
        In this case, prepare content for grub legacy boot partition.
        """
        if not kernel_dir:
            kernel_dir = get_bitbake_var("DEPLOY_DIR_IMAGE")
            if not kernel_dir:
                raise WicError("Couldn't find DEPLOY_DIR_IMAGE, exiting")

        staging_kernel_dir = kernel_dir

        hdddir = "%s/hdd/boot" % cr_workdir

        install_cmd = "install -m 0644 %s/bzImage %s/bzImage" % \
            (staging_kernel_dir, hdddir)
        exec_cmd(install_cmd)
        shutil.copyfile("%s/hdd/boot/grub/grub.cfg" % cr_workdir,
                        "%s/grub.cfg" % cr_workdir)
        shutil.move("%s/grub.cfg" % cr_workdir,
                    "%s/hdd/boot/grub/grub.cfg" % cr_workdir)

        startup = os.path.join(kernel_dir, "startup.nsh")
        if os.path.exists(startup):
            cp_cmd = "cp %s %s/" % (startup, hdddir)
            exec_cmd(cp_cmd, True)

        du_cmd = "du -bks %s" % hdddir
        out = exec_cmd(du_cmd)
        blocks = int(out.split()[0])

        extra_blocks = part.get_extra_block_count(blocks)

        if extra_blocks < BOOTDD_EXTRA_SPACE:
            extra_blocks = BOOTDD_EXTRA_SPACE

        blocks += extra_blocks

        logger.debug("Added %d extra blocks to %s to get to %d total blocks",
                     extra_blocks, part.mountpoint, blocks)

        # dosfs image, created by mkdosfs
        bootimg = "%s/boot.img" % cr_workdir

        label = part.label if part.label else "ESP"

        dosfs_cmd = "mkdosfs -n %s -i %s -C %s %d" % \
                    (label, part.fsuuid, bootimg, blocks)
        exec_native_cmd(dosfs_cmd, native_sysroot)

        mcopy_cmd = "mcopy -i %s -s %s/* ::/" % (bootimg, hdddir)
        exec_native_cmd(mcopy_cmd, native_sysroot)

        chmod_cmd = "chmod 644 %s" % bootimg
        exec_cmd(chmod_cmd)

        du_cmd = "du -Lbks %s" % bootimg
        out = exec_cmd(du_cmd)
        bootimg_size = out.split()[0]

        part.size = int(bootimg_size)
        part.source_file = bootimg
