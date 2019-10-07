SUMMARY = "pfsense preinstalled image"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

SRC_URI = "file://pfsense.img"

SRC_URI[md5sum] = "0e94eb17fd595d8f54b600e7c9ac45c0"
SRC_URI[sha256sum] = "6fffefa0b09daea397e83f67bf730392125b720043c455597c05d3d80c2baa29"

do_install() {
    install -d ${D}${datadir}/xen-images
    install -m 0644 ${WORKDIR}/pfsense.img ${D}${datadir}/xen-images/
}

FILES_${PN} += "${datadir}/xen-images/pfsense.img"
