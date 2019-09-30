SUMMARY = "Systemd networkd configs"
DESCRIPTION = "Systemd networkd configs"
HOMEPAGE = ""
LICENSE = "CLOSED"

SRC_URI = " \
    file://xenbr0.network \
    file://xenbr0.netdev \
    file://80-wired.network \
    file://vif.network \
"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${sysconfdir}/systemd/network
    install -m  0644 ${S}/xenbr0.network ${D}${sysconfdir}/systemd/network
    install -m  0644 ${S}/xenbr0.netdev ${D}${sysconfdir}/systemd/network
    install -m  0644 ${S}/80-wired.network ${D}${sysconfdir}/systemd/network
    install -m  0644 ${S}/vif.network ${D}${sysconfdir}/systemd/network
}

FILES_${PN} += "${sysconfdir}"
