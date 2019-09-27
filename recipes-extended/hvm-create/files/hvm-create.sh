#!/usr/bin/env bash

usage () {
    echo "Usage: hvm-create [-d] <LVM device name>"
    echo "example: hvm-create -d sda3"
    echo "-h | --help           print this message"
    echo "-d | --device         LVM device assignment"
}

while [ "$1" != "" ]; do
    case $1 in
        -d | --device )
            shift
            device=$1
            ;;
        -h | --help )
            usage
            exit
            ;;
        * )
            usage
            exit 1
    esac
    shift
done

if [ -z "$device" ]; then
    usage
    exit 1
fi


XEN_IMAGES="/usr/share/xen-images"
OPNSENSE_IMAGE="OPNsense-19.7-OpenSSL-nano-amd64.img"

if [ -f "${XEN_IMAGES}/${OPNSENSE_IMAGE}.bz2" ]; then
    pushd ${XEN_IMAGES}
    echo "Uncompressing ${OPNSENSE_IMAGE}.bz2"
    bzip2 -d ${OPNSENSE_IMAGE}.bz2
    echo "done"
    popd
fi

vgremove vg0 -y
vgcreate vg0 /dev/$device
lvcreate -n ndvm-1 -L 512M vg0
lvcreate -n ndvm-2 -L 512M vg0
lvcreate -n ndvm-3 -L 512M vg0
lvcreate -n opn-sense -L 6G vg0
xl pci-assignable-add 02:00.0
xl pci-assignable-add 03:00.0
xl pci-assignable-add 04:00.0

xl create hvm-conf/ndvm-1.cfg
sleep 90
xl create hvm-conf/ndvm-2.cfg
sleep 90
xl create hvm-conf/ndvm-3.cfg
sleep 90
xl create hvm-conf/opnsense.cfg
