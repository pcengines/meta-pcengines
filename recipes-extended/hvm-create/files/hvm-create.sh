#!/bin/sh

vgchange -a y vg0
xl pci-assignable-add 02:00.0
xl pci-assignable-add 03:00.0
xl pci-assignable-add 04:00.0

xl create /home/root/hvm-conf/ndvm-1.cfg
xl create /home/root/hvm-conf/ndvm-2.cfg
xl create /home/root/hvm-conf/ndvm-3.cfg
sleep 90
xl create /home/root/hvm-conf/pfsense.cfg
