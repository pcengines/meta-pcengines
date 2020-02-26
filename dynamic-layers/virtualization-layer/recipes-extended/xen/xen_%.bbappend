do_deploy_append() {
    if [ -f ${DEPLOYDIR}/xen-${MACHINE}.gz  ]; then
        rm -f ${DEPLOYDIR}/xen.gz
        ln -s xen-${MACHINE}.gz ${DEPLOYDIR}/xen.gz
    fi
}
