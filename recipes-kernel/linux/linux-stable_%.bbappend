FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = " file://defconfig"

# Allow to set up a 5GHz AP on recent kernels
# https://github.com/pcengines/apu2-documentation/issues/189
SRC_URI_append = " file://0001-wireless-ath-optional-regulatory-domain.patch"

KCONFIG_MODE = "alldefconfig"

KERNEL_DANGLING_FEATURES_WARN_ONLY = "1"
