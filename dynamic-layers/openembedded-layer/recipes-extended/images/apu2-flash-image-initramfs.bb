require recipes-core/images/core-image-minimal.bb

IMAGE_INSTALL:append = " \
  flashrom \
  gnupg \
  wget \
  ca-certificates \
  bmap-tools \
  libgcc \
  "

IMAGE_FSTYPES += "cpio.gz"
IMAGE_FEATURES:append = " ssh-server-openssh"
