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
  dhcp-client \
  netcat \
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

IMAGE_ROOTFS_EXTRA_SPACE = "2097152"

ROOTFS_POSTPROCESS_COMMAND += "rootfs_install_ndvm_image; "

do_rootfs[depends] += "xen-ndvm-image:do_image_complete"

rootfs_install_ndvm_image(){
    install -d ${IMAGE_ROOTFS}/${datadir}/xen-images/
    install ${DEPLOY_DIR_IMAGE}/xen-ndvm-image-${MACHINE}.hddimg ${IMAGE_ROOTFS}/${datadir}/xen-images/xen-ndvm-image-1.hddimg
    install ${DEPLOY_DIR_IMAGE}/xen-ndvm-image-${MACHINE}.hddimg ${IMAGE_ROOTFS}/${datadir}/xen-images/xen-ndvm-image-2.hddimg
    install ${DEPLOY_DIR_IMAGE}/xen-ndvm-image-${MACHINE}.hddimg ${IMAGE_ROOTFS}/${datadir}/xen-images/xen-ndvm-image-3.hddimg
}

IMAGE_FSTYPES += "wic.gz wic.bmap"
