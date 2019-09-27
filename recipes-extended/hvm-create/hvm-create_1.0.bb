SUMMARY = "HVM create"
DESCRIPTION = "HVM create"
HOMEPAGE = ""
LICENSE = "CLOSED"
HVM_SH := "${THISDIR}/files/hvm-create.sh"
HVM_CONFIG := "${THISDIR}/files/xen-guest-minimal.cfg"
HVM_CONFIG2 := "${THISDIR}/files/xen-guest-minimal2.cfg"
HVM_CONFIG3 := "${THISDIR}/files/xen-guest-minimal3.cfg"
OPN_SENSE := "${THISDIR}/files/opn-sense.cfg"

do_install() {
    install -d ${D}${ROOT_HOME}
    install -d ${D}${ROOT_HOME}/hvm-conf
    install -m  0755 ${HVM_SH} ${D}${ROOT_HOME}
    install -m  0644 ${HVM_CONFIG} ${D}${ROOT_HOME}/hvm-conf
    install -m  0644 ${HVM_CONFIG2} ${D}${ROOT_HOME}/hvm-conf
    install -m  0644 ${HVM_CONFIG3} ${D}${ROOT_HOME}/hvm-conf
    install -m  0644 ${OPN_SENSE} ${D}${ROOT_HOME}/hvm-conf
}

FILES_${PN} += "${ROOT_HOME}/hvm-conf"
FILES_${PN} += "${ROOT_HOME}"