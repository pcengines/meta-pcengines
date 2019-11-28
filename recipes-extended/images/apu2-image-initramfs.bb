require recipes-core/images/core-image-minimal-initramfs.bb

IMAGE_INSTALL_append = " \
  flashrom \
  gnupg \
  wget \
  ca-certificates \
  "

IMAGE_FEATURES_append = " ssh-server-openssh"
