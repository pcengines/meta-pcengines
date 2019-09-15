require recipes-extended/images/core-image-full-cmdline.bb

IMAGE_INSTALL_append = " \
  xen-base \
  xen-misc \
  tpm2-tools \
  tpm2-abrmd \
  tpm2-tss \
  libtss2 \
  libtss2-mu \
  libtss2-tcti-device \
  libtss2-tcti-mssim \
  "
