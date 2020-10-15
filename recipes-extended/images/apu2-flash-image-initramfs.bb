require recipes-core/images/core-image-minimal.bb

IMAGE_INSTALL_append = " \
  flashrom \
  gnupg \
  wget \
  ca-certificates \
  bmap-tools \
  libgcc \
  "

IMAGE_FSTYPES += "cpio.gz"
IMAGE_FEATURES_append = " ssh-server-openssh"
