#
# SPDX-License-Identifier: GPL-2.0-only
#
# DESCRIPTION
# This implements the 'bootimg-grub-tb' source plugin class for 'wic'
# Support for Trenchboot
#
# AUTHORS
# Norbert Kamiński <norbert.kaminski (at) 3mbeb.com>
#
# This file is derived from bootimg-efi.py and bootimg-pcbios.py by:
#   Tom Zanussi <tom.zanussi (at] linux.intel.com>

import logging
import os
import shutil
import gzip

from wic import WicError
from wic.engine import get_custom_config
from wic.pluginbase import SourcePlugin
from wic.misc import (exec_cmd, exec_native_cmd,
                      get_bitbake_var, BOOTDD_EXTRA_SPACE)

logger = logging.getLogger('wic')


class BootimgGrubTbPlugin(SourcePlugin):
    """
    Create partition for Grub-tb.
    """

    name = 'bootimg-grub-tb'

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
    def do_install_disk(cls, disk, disk_name, creator, workdir, oe_builddir,
                        bootimg_dir, kernel_dir, native_sysroot):
        """
        Called after all partitions have been prepared and assembled into a
        disk image.  In this case, we install the MBR.
        """

        bootimg_dir = cls._get_bootimg_dir(bootimg_dir, 'syslinux')
        mbrfile = "%s/syslinux/" % bootimg_dir
        mbrfile += "mbr.bin"

        full_path = creator._full_path(workdir, disk_name, "direct")
        logger.debug("Installing MBR on disk %s as %s with size %s bytes",
                     disk_name, full_path, disk.min_size)

        device_map_path = "%s/device.map" % workdir
        device_map_content = "(hd0) %s" % full_path
        with open(device_map_path, 'w') as file:
            file.write(device_map_content)

        dd_cmd = "dd if=%s of=%s conv=notrunc" % (mbrfile, full_path)
        exec_cmd(dd_cmd, native_sysroot)

        grub_dir = "%s/hdd/boot/grub/i386-pc" % workdir
        cmd_bios_setup = 'grub-bios-setup -v --device-map=%s -r "hd0,msdos1" -d %s %s' % (
                          device_map_path,
                          grub_dir,
                          full_path
                          )
        exec_cmd(cmd_bios_setup, native_sysroot)

    @classmethod
    def do_install_core_image(cls, grubdir ,native_sysroot):
        """
        Create the core image in the grub directory.
        """
        grub_modules = "at_keyboard biosdisk boot chain configfile ext2 fat linux ls part_msdos reboot serial vga"
        cmd_mkimage = "grub-mkimage -p %s -d %s/i386-pc -o %s/i386-pc/core.img -O i386-pc %s" % (
                       "(hd0,msdos1)/grub",
                       grubdir,
                       grubdir,
                       grub_modules)

        exec_cmd(cmd_mkimage)

    @classmethod
    def do_configure_grub_legacy(cls, hdddir, creator, cr_workdir,
                                 source_params):
        """
        Check if custom config exists in deploy dir, if not create config file.
        """

        # Create config file
        bootloader = creator.ks.bootloader
        hdddir = "%s/hdd/boot/grub" % cr_workdir

        install_cmd = "install -d %s" % hdddir
        exec_cmd(install_cmd)

        deploy_dir = get_bitbake_var("DEPLOY_DIR_IMAGE")
        grub_cfg_dir = "%s/%s" % (deploy_dir, "grub.cfg")
        xen_gz_dir = "%s/%s" % (deploy_dir, "xen.gz")

        if os.path.exists(grub_cfg_dir):
            shutil.copyfile(grub_cfg_dir, "%s/grub.cfg" % hdddir)
        elif os.path.exists(xen_gz_dir):
            initrd = source_params.get('initrd')

            grub_conf = ""
            grub_conf += "serial --unit=0 --speed=115200\n"
            grub_conf += "terminal --timeout=%s serial\n" % bootloader.timeout
            grub_conf += "default=boot\n"
            grub_conf += "menuentry 'boot-xen' {\n"

            xen = "/xen"
            kernel = "/bzImage"
            bootdev = "(hd0,msdos1)"
            dom0_conf = "dom0_mem=2G loglvl=all guest_loglvl=all"
            dom0_serial = "com1=115200,8n1 console=com1 no-real-mode"
            rootdev = "/dev/sda2"
            kernel_params = "console=hvc0 earlyprintk=xen nomodeset"

            grub_conf += "  insmod part_msdos\n"
            grub_conf += "  set root=%s\n" % bootdev
            grub_conf += "  multiboot2 %s %s %s\n" \
                % (xen, dom0_conf, dom0_serial)
            grub_conf += "  module2 %s root=%s %s\n" \
                % (kernel, rootdev, kernel_params)

            if initrd:
                grub_conf += "  module2 initrd /%s\n" % initrd

            grub_conf += "}\n"

            # Secure launch
            grub_conf += "\n"
            grub_conf += "menuentry 'secure-boot-xen' {\n"
            grub_conf += "  insmod part_msdos\n"
            grub_conf += "  set root=%s\n" % bootdev
            grub_conf += "  slaunch skinit\n"
            grub_conf += "  slaunch_module %s/skl.bin\n" % bootdev
            grub_conf += "  multiboot2 %s %s %s\n" \
                % (xen, dom0_conf, dom0_serial)
            grub_conf += "  module2 %s root=%s %s\n" \
                % (kernel, rootdev, kernel_params)

            if initrd:
                grub_conf += "  module2 initrd /%s\n" % initrd

            grub_conf += "}\n"

            logger.debug("Writing grub config %s/hdd/boot/grub/grub.cfg",
                        cr_workdir)
            cfg = open("%s/hdd/boot/grub/grub.cfg" % cr_workdir, "w")
            cfg.write(grub_conf)
            cfg.close()
        else:
            initrd = source_params.get('initrd')

            grub_conf = ""
            grub_conf += "serial --unit=0 --speed=115200\n"
            grub_conf += "terminal --timeout=%s serial\n" % bootloader.timeout
            grub_conf += "default=boot\n"
            grub_conf += "menuentry 'boot' {\n"

            kernel = "/bzImage"
            bootdev = "(hd0,msdos1)"
            rootdev = "/dev/sda2"
            serial = "console=ttyS0,115200 earlyprintk=serial,ttyS0,115200"

            grub_conf += "  linux %s root=%s %s\n" \
                % (kernel, rootdev, serial)

            if initrd:
                grub_conf += "    initrd /%s\n" % initrd

            grub_conf += "}\n"

            # Secure launch
            grub_conf += "\n"
            grub_conf += "menuentry 'secure-boot' {\n"
            grub_conf += "  slaunch skinit\n"
            grub_conf += "  slaunch_module %s/skl.bin\n" % bootdev
            grub_conf += "  linux %s root=%s %s\n" \
                % (kernel, rootdev, serial)

            if initrd:
                grub_conf += "    initrd /%s\n" % initrd

            grub_conf += "}\n"

            logger.debug("Writing grub config %s/hdd/boot/grub/grub.cfg",
                        cr_workdir)
            cfg = open("%s/hdd/boot/grub/grub.cfg" % cr_workdir, "w")
            cfg.write(grub_conf)
            cfg.close()

        # Check if custom grubenv file exists
        grubenv_dir = "%s/%s" % (deploy_dir, "grubenv")
        if os.path.exists(grubenv_dir):
            shutil.copyfile(grubenv_dir, "%s/grubenv" % hdddir)

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

        # Copying kernel
        hdddir = "%s/hdd/boot" % cr_workdir
        install_cmd = "install -m 0644 %s/bzImage %s/bzImage" % \
            (staging_kernel_dir, hdddir)
        exec_cmd(install_cmd)

        # Copying lz_header
        install_cmd = "install -m 0600 %s/skl.bin %s/skl.bin" % \
            (staging_kernel_dir, hdddir)
        exec_cmd(install_cmd)

        # Copying grub modules
        grub_dir_native = get_bitbake_var("IMAGE_ROOTFS") + "/usr/lib64/grub-tb"
        shutil.copytree("%s/i386-pc" % (grub_dir_native),
                        "%s/grub/i386-pc" % hdddir)

        # Copying xen module if exists
        if os.path.exists("%s/xen.gz" % staging_kernel_dir):
            install_cmd = "install -m 0644 %s/xen.gz %s/xen.gz" % \
                (staging_kernel_dir, hdddir)
            exec_cmd(install_cmd)
            # Uncompressing xen
            with gzip.open('%s/xen.gz' % hdddir, 'rb') as f_in:
                with open('%s/xen' % hdddir, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

        # Creating core.img
        grub_dir_hdd = "%s/grub" % hdddir
        cls.do_install_core_image(grub_dir_hdd, native_sysroot)

        # Counting size
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
