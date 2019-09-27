require recipes-extended/images/xen-guest-image-minimal.bb

IMAGE_INSTALL_append = " \
  xen-base \
  iperf3 \
  openssh \
  bridge-utils \
  openvswitch \
  ifupdown \
  kernel-modules \
  iptables \
  wget \
  ethtool \
  iputils-ping \
  "
