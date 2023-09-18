DESCRIPTION = "Mainline Linux Kernel"
SECTION = "kernel"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${S}/COPYING;md5=bbea815ee2795b2f4230826c0c6b8814"

inherit kernel
require recipes-kernel/linux/linux-yocto.inc

LINUX_VERSION_EXTENSION = ""

SRC_URI = " \
    git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git;branch=${KBRANCH};tag=${LINUX_TAG} \
    git://git.yoctoproject.org/yocto-kernel-cache;type=kmeta;name=meta;branch=yocto-5.4;destsuffix=kernel-meta \
    file://defconfig \
    "

SRCREV_meta = "aafb8f095e97013d6e55b09ed150369cbe0c6476"

PV = "${LINUX_VERSION}+git${SRCPV}"

# S = "${WORKDIR}/git"

KCONFIG_MODE="--alldefconfig"

# The oldnoconfig has been replaced with the olddefconfig command
# see: https://patchwork.kernel.org/patch/10172375/
# KERNEL_CONFIG_COMMAND = "oe_runmake_call -C ${S} CC="${KERNEL_CC}" O=${B} olddefconfig"
# FILES:${KERNEL_PACKAGE_NAME}-base += "${nonarch_base_libdir}/modules/${KERNEL_VERSION}/modules.builtin.modinfo"

COMPATIBLE_MACHINE:pcengines-apu2 = "pcengines-apu2"
