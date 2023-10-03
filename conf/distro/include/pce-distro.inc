require conf/distro/poky.conf

DISTRO_NAME = "Reference Yocto distro for PC Engines hardware"
DISTRO_VERSION = "0.2"
SDK_VENDOR = "-pcesdk"
TARGET_VENDOR = "-pce"

MAINTAINER = "maciej.pijanowski@3mdeb.com"

DISTRO_FEATURES = " \
    ext2 \
    keyboard \
    largefile \
    ldconfig \
    nfs \
    pci \
    systemd \
    usbgadget \
    usbhost \
    virtualization \
    seccomp \
"

# disable sysvinit
VIRTUAL-RUNTIME_init_manager = "systemd"
VIRTUAL-RUNTIME_initscripts = ""
VIRTUAL-RUNTIME_syslog = ""
DISTRO_FEATURES_BACKFILL_CONSIDERED += "sysvinit"

PREFERRED_VERSION_linux-yocto ?= "4.19%"
