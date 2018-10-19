PREFERRED_PROVIDER_virtual/kernel ?= "linux-yocto"

# provides gcc tune for Family 16h
require conf/machine/include/tune-family16h.inc

MULTILIBS ?= ""
require conf/multilib.conf

# Add serial consoles to kernel commandline
KERNEL_SERIAL_CONSOLE ??= "console=ttyS0,115200n8"
APPEND += "${KERNEL_SERIAL_CONSOLE}"

MACHINEOVERRIDES =. "amd:amdx86:pcengines-apux:"

# Metadata used by CodeBench for the ADE
ADE_CB_CPU = "general.cpu.jaguar"

XSERVER ?= "${XSERVER_X86_BASE} \
            ${XSERVER_X86_EXT} \
            ${XSERVER_X86_FBDEV} \
           "

PREFERRED_VERSION_linux-yocto = "4.14%"

MACHINE_FEATURES += " \
    efi \
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

IMAGE_FSTYPES += "ext4"

IMAGE_OVERHEAD_FACTOR = "1.1"
