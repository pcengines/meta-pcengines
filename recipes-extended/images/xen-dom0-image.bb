require recipes-extended/images/xen-image-minimal.bb

IMAGE_INSTALL_append = " \
  kernel-modules \
  xen-misc \
  tpm2-tools \
  tpm2-abrmd \
  tpm2-tss \
  libtss2 \
  libtss2-mu \
  libtss2-tcti-device \
  libtss2-tcti-mssim \
  grub \
  lvm2 \
  bridge-utils \
  seabios \
  hvm-create \
  openvswitch \
  opnsense \
  "

build_syslinux_cfg () {
	echo "ALLOWOPTIONS 1" > ${SYSLINUX_CFG}
	echo "DEFAULT boot" >> ${SYSLINUX_CFG}
	echo "TIMEOUT 10" >> ${SYSLINUX_CFG}
	echo "PROMPT 1" >> ${SYSLINUX_CFG}
	echo "LABEL boot" >> ${SYSLINUX_CFG}
	echo "  KERNEL mboot.c32" >> ${SYSLINUX_CFG}
	echo "  APPEND /xen.gz dom0_mem=512M ${SYSLINUX_XEN_ARGS} --- /${KERNEL_IMAGETYPE} ${SYSLINUX_KERNEL_ARGS} --- /initrd" >> ${SYSLINUX_CFG}
}


ROOTFS_POSTPROCESS_COMMAND += "rootfs_install_ndvm_image; "

do_image[depends] += "xen-ndvm-image:do_build"

rootfs_install_ndvm_image(){
    install -d ${IMAGE_ROOTFS}/${datadir}/xen-images/
    install ${DEPLOY_DIR_IMAGE}/xen-ndvm-image-${MACHINE}.hddimg ${IMAGE_ROOTFS}/${datadir}/xen-images/xen-ndvm-image.hddimg
}
