FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI += "file://hostapd.conf"

do_install_append() {
    rm ${D}${sysconfdir}/hostapd.conf
    install -m 0644 ${WORKDIR}/hostapd.conf ${D}${sysconfdir}
    install -m 0644 ${WORKDIR}/hostapd-ac.conf ${D}${sysconfdir}
}
