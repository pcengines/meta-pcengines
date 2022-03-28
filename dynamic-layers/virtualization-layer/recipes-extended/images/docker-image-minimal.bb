require recipes-core/images/core-image-minimal.bb

IMAGE_INSTALL:append = " \
  docker-ce \
  less \
  "

IMAGE_FEATURES:append = " ssh-server-openssh"
