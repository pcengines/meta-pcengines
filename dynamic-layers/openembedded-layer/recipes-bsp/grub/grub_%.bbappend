BBCLASSEXTEND = "native"
FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI += " \
    file://0001-add-root-flag-to-grub-bios-setup.patch \
"
