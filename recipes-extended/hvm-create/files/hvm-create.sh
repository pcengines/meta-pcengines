#!/usr/bin/env bash

device=""

usage () {
    echo "Usage: hvm-create [-d] <LVM device name>"
    echo "example: hvm-create -d sdb1"
    echo "-h | --help           print this message"
    echo "-d | --device         LVM device assignment"   
}

while [ "$1" != "" ]; do
    case $1 in
        -d | --device )     shift
                            device=$1
                            ;;
        -h | --help )       usage
                            exit
                            ;;
        * )                 usage
                            exit 1
    esac
    shift
done

if [ "$device" == "" ]; then

    usage
    exit 1

fi

vgremove vg0 -y
vgcreate vg0 /dev/$device
lvcreate -n xen-guest-minimal -L 10G vg0
lvcreate -n xen-guest-minimal2 -L 10G vg0
lvcreate -n xen-guest-minimal3 -L 10G vg0
lvcreate -n opn-sense -L 10G vg0
xl pci-assignable-add 03:00.0
xl pci-assignable-add 02:00.0
xl pci-assignable-add 04:00.0
mount /dev/mmcblk0 /mnt

xl create hvm-conf/xen-guest-minimal.cfg
sleep 90
xl create hvm-conf/xen-guest-minimal2.cfg
sleep 90
xl create hvm-conf/xen-guest-minimal3.cfg
sleep 90
xl create hvm-conf/opn-sense.cfg
