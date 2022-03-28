SUMMARY = "flashrom"
DESCRIPTION = "flashrom is a utility for identifying, reading, writing, verifying and erasing flash chips"
LICENSE = "CLOSED"
HOMEPAGE = "https://github.com/pcengines/flashrom"

SRC_URI = "git://github.com/pcengines/flashrom.git;branch=apu_support "
SRCREV = "d66dae14acbb7a5288e06921e28153b24990ae64"

DEPENDS = "pciutils libusb libusb-compat"

PV = "1.0.1-pcengines+${SRCPV}"

S = "${WORKDIR}/git"

inherit pkgconfig


do_install() {
    oe_runmake PREFIX=${prefix} DESTDIR=${D} install
}
