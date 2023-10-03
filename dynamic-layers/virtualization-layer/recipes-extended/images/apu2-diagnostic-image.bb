require docker-image-minimal.bb

IMAGE_INSTALL:append = " \
    flashrom \
    edac-utils \
    tpm2-tools \
    tpm2-abrmd \
    tpm2-tss \
    libtss2 \
    libtss2-mu \
    libtss2-tcti-device \
    libtss2-tcti-mssim \
    git \
    packagegroup-core-buildessential \
  "
