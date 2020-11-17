PREFERRED_PROVIDER_virtual/kernel ?= "linux-yocto"

# provides gcc tune for Family 16h
require conf/machine/include/tune-dbft3b.inc

# Add serial consoles to kernel commandline
SERIAL_CONSOLES = "115200;ttyS0"
KERNEL_SERIAL_CONSOLE ??= "console=ttyS0,115200n8"
APPEND += "${KERNEL_SERIAL_CONSOLE}"

MACHINEOVERRIDES =. "amd:amdx86:pcengines-apux:"

# Metadata used by CodeBench for the ADE
ADE_CB_CPU = "general.cpu.jaguar"

XSERVER ?= "${XSERVER_X86_BASE} \
            ${XSERVER_X86_EXT} \
            ${XSERVER_X86_FBDEV} \
           "

PREFERRED_PROVIDER_virtual/kernel = "linux-stable"
PREFERRED_VERSION_linux-yocto = "5.4%"

MACHINE_FEATURES += " \
    rtc \
    pcbios \
    vfat \
    tpm \
    tpm2 \
    txt \
    ima \
"

MACHINE_EXTRA_RRECOMMENDS += " \
    kernel-modules \
    grub \
    parted \
    util-linux-blkid \
"

# QEMU does not support some of the enhanced instructions available
# on the AMD chips which causes some build time failures.
# Such as:
# NOTE: > Executing update_gio_module_cache intercept ...
# NOTE: Exit code 132. Output:
# Illegal instruction (core dumped)
MACHINE_FEATURES_remove = "qemu-usermode"

APPEND_ADDITIONAL ??= ""
APPEND += "${APPEND_ADDITIONAL}"

IMAGE_FSTYPES += "ext4 wic.gz wic.bmap"

IMAGE_OVERHEAD_FACTOR = "1.1"

KERNEL_IMAGETYPE = "bzImage"

KERNEL_MODULE_AUTOLOAD_pce-xen += " \
    xen-netback \
    xen_wdt \
    xen-gntdev \
    xen-gntalloc \
    en-acpi-processor \
    xen-pciback \
    xen-blkback \
"

WKS_FILES ?= "directdisk-grub-legacy.wks"
