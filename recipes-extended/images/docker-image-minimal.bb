require recipes-core/images/core-image-minimal.bb

IMAGE_INSTALL_append = " \
  docker-ce \
  less \
  openssh \
  "
