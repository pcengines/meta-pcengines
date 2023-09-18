DESCRIPTION = "Mainline Linux Kernel"
SECTION = "kernel"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${S}/COPYING;md5=6bc538ed5bd9a7fc9398086aedcd7e46"

inherit kernel
require recipes-kernel/linux/linux-yocto.inc

LINUX_VERSION_EXTENSION = ""

SRC_URI = " \
    git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git;branch=${KBRANCH};tag=${LINUX_TAG} \
    git://git.yoctoproject.org/yocto-kernel-cache;type=kmeta;name=meta;branch=yocto-5.15;destsuffix=kernel-meta \
    file://defconfig \
    "

SRCREV_meta = "f484a7f175b4f3c4f7d2b553cde232bd41f757d8"

PV = "${LINUX_VERSION}+git${SRCPV}"

# S = "${WORKDIR}/git"

KCONFIG_MODE="--alldefconfig"

# The oldnoconfig has been replaced with the olddefconfig command
# see: https://patchwork.kernel.org/patch/10172375/
# KERNEL_CONFIG_COMMAND = "oe_runmake_call -C ${S} CC="${KERNEL_CC}" O=${B} olddefconfig"
# FILES:${KERNEL_PACKAGE_NAME}-base += "${nonarch_base_libdir}/modules/${KERNEL_VERSION}/modules.builtin.modinfo"

COMPATIBLE_MACHINE:pcengines-apu2 = "pcengines-apu2"
