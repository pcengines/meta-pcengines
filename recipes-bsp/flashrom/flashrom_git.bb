SUMMARY = "flashrom"
DESCRIPTION = "flashrom is a utility for identifying, reading, writing, verifying and erasing flash chips"
LICENSE = "CLOSED"
HOMEPAGE = "https://github.com/pcengines/flashrom"

SRC_URI = "git://github.com/pcengines/flashrom.git;branch=apu_support "
SRCREV = "092b1c28bf31dab170d2fc0dc09b6bee3fa68bfa"

DEPENDS = "pciutils libusb libusb-compat"

PV = "1.0.1-pcengines+${SRCPV}"

S = "${WORKDIR}/git"

inherit pkgconfig


do_install() {
    oe_runmake PREFIX=${prefix} DESTDIR=${D} install
}
