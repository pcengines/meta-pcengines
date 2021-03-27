FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = "file://defconfig"

KCONFIG_MODE = "alldefconfig"

KERNEL_DANGLING_FEATURES_WARN_ONLY = "1"
