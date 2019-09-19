FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

require recipes-bsp/grub/grub2.inc

BRANCH = "fix_duplicated_syms"
SRC_URI_remove = " ${GNU_MIRROR}/grub/grub-${PV}.tar.gz"
SRC_URI_append = " git://github.com/3mdeb/grub2.git;branch=${BRANCH};protocol=https"


S = "${WORKDIR}/git"

SRCREV = "b724a59276eb0bd6b11f01a2819af84649b38ce5"

PV = "2.0.4-rc1+${SRCREV}"

RDEPENDS_${PN}-common += "${PN}-editenv"
RDEPENDS_${PN} += "diffutils freetype ${PN}-common"

RPROVIDES_${PN}-editenv += "${PN}-efi-editenv"

PACKAGES =+ "${PN}-editenv ${PN}-common"
FILES_${PN}-editenv = "${bindir}/grub-editenv"
FILES_${PN}-common = " \
    ${bindir} \
    ${sysconfdir} \
    ${sbindir} \
    ${datadir}/grub \
"

FILES_${PN}-common_append_aarch64 = " \
    ${libdir}/${BPN} \
"

# grub is blackisted in
# meta/conf/distro/include/security_flags.inc 
# it won't compile with security flags enabled
SECURITY_CFLAGS = ""

do_configure_prepend() {
	( cd ${S}
	${S}/bootstrap
	${S}/autogen.sh )
}

do_install_append () {
    install -d ${D}${sysconfdir}/grub.d
    # Remove build host references...
    find "${D}" -name modinfo.sh -type f -exec \
        sed -i \
        -e 's,--sysroot=${STAGING_DIR_TARGET},,g' \
        -e 's|${DEBUG_PREFIX_MAP}||g' \
        -e 's:${RECIPE_SYSROOT_NATIVE}::g' \
        {} +
}

INSANE_SKIP_${PN} = "arch"
INSANE_SKIP_${PN}-dbg = "arch"
