require recipes-kernel/linux/linux-stable.inc

LINUX_VERSION = "5.4.42"
LINUX_TAG = "v${LINUX_VERSION}"
KERNEL_VERSION_SANITY_SKIP="1"

KBRANCH = "linux-5.4.y"

DEPENDS += "elfutils-native"
