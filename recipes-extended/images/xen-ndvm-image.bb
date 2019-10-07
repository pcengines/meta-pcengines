require recipes-extended/images/xen-guest-image-minimal.bb

IMAGE_INSTALL_append = " \
  xen-base \
  xen-misc \
  iperf3 \
  openssh \
  bridge-utils \
  openvswitch \
  kernel-modules \
  iptables \
  wget \
  ethtool \
  iputils-ping \
  xen-ndvm-networkd-config \
  tcpdump \
  xen-libxenstore \
  xen-xenstore \
  wget \
  dhcp-client \
  netcat \
  "
