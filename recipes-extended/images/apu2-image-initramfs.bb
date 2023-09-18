require recipes-core/images/core-image-minimal.bb

IMAGE_INSTALL:append = " \
  flashrom \
  gnupg \
  wget \
  ca-certificates \
  "

IMAGE_FEATURES:append = " ssh-server-openssh"
