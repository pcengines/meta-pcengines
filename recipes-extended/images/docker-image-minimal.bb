require recipes-core/images/core-image-minimal.bb

IMAGE_INSTALL_append = " \
  docker-ce \
  less \
  "

IMAGE_FEATURES_append = " ssh-server-openssh"
