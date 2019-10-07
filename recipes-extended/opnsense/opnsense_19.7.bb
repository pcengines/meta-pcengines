SUMMARY = "OPNsense nano image"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

SRC_URI = "https://mirror.dns-root.de/opnsense/releases/19.7/OPNsense-19.7-OpenSSL-nano-amd64.img.bz2;unpack=no"

SRC_URI[md5sum] = "0e94eb17fd595d8f54b600e7c9ac45c0"
SRC_URI[sha256sum] = "6fffefa0b09daea397e83f67bf730392125b720043c455597c05d3d80c2baa29"

do_install() {
    install -d ${D}${datadir}/xen-images
    install -m 0644 ${WORKDIR}/OPNsense-19.7-OpenSSL-nano-amd64.img.bz2 ${D}${datadir}/xen-images
}

FILES_${PN} += "${datadir}/xen-images/OPNsense-19.7-OpenSSL-nano-amd64.img.bz2"
