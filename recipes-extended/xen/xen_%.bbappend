FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI_append = " file://0001-always-enable-AMD_IOMMU_DEBUG.patch"
SRC_URI_append = " file://0002-always-enable-AMD_IOMMU_DEBUG.patch"

do_deploy_append() {
    if [ -f ${DEPLOYDIR}/xen-${MACHINE}.gz  ]; then
        ln -s xen-${MACHINE}.gz ${DEPLOYDIR}/xen.gz
    fi
}
