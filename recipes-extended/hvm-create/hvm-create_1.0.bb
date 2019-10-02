SUMMARY = "HVM create"
DESCRIPTION = "HVM create"
HOMEPAGE = ""
LICENSE = "CLOSED"

SRC_URI = " \
  file://ndvm-1.cfg \
  file://ndvm-2.cfg \
  file://ndvm-3.cfg \
  file://opnsense.cfg \
  file://pfsense.cfg \
  file://hvm-create.sh \
"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${ROOT_HOME}/hvm-conf
    install -m  0755 ${S}/hvm-create.sh ${D}${ROOT_HOME}
    install -m  0644 ${S}/ndvm-1.cfg ${D}${ROOT_HOME}/hvm-conf/
    install -m  0644 ${S}/ndvm-2.cfg ${D}${ROOT_HOME}/hvm-conf/
    install -m  0644 ${S}/ndvm-3.cfg ${D}${ROOT_HOME}/hvm-conf/
    install -m  0644 ${S}/opnsense.cfg ${D}${ROOT_HOME}/hvm-conf/
    install -m  0644 ${S}/pfsense.cfg ${D}${ROOT_HOME}/hvm-conf/
}

FILES_${PN} += "${ROOT_HOME}/hvm-conf/ ${ROOT_HOME}/hvm-create.sh"

RDEPENDS_${PN} += "bash"
