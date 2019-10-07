FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI_append = " \
    file://0001-always-enable-AMD_IOMMU_DEBUG.patch \
    file://0002-always-enable-AMD_IOMMU_DEBUG.patch \
    file://0001-Enable-more-verbose-debug.patch \
"

OECMAKE_C_FLAGS_RELEASE_append = " -DNDEBUG"

do_deploy_append() {
    if [ -f ${DEPLOYDIR}/xen-${MACHINE}.gz  ]; then
        rm -f ${DEPLOYDIR}/xen.gz
        ln -s xen-${MACHINE}.gz ${DEPLOYDIR}/xen.gz
    fi
}
