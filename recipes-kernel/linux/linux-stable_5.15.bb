require recipes-kernel/linux/linux-stable.inc

LINUX_VERSION = "5.15.124"
LINUX_TAG = "v${LINUX_VERSION}"
KERNEL_VERSION_SANITY_SKIP="1"

KBRANCH = "linux-5.15.y"

DEPENDS += "elfutils-native"
