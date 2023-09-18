require recipes-extended/images/xen-image-minimal.bb

IMAGE_INSTALL:append = " \
  seabios \
  "

build_syslinux_cfg () {
	echo "ALLOWOPTIONS 1" > ${SYSLINUX_CFG}
	echo "DEFAULT boot" >> ${SYSLINUX_CFG}
	echo "TIMEOUT 10" >> ${SYSLINUX_CFG}
	echo "PROMPT 1" >> ${SYSLINUX_CFG}
	echo "LABEL boot" >> ${SYSLINUX_CFG}
	echo "  KERNEL mboot.c32" >> ${SYSLINUX_CFG}
	echo "  APPEND /xen.gz dom0_mem=1024M ${SYSLINUX_XEN_ARGS} --- /${KERNEL_IMAGETYPE} ${SYSLINUX_KERNEL_ARGS} --- /initrd" >> ${SYSLINUX_CFG}
}
