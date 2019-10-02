#!/bin/bash

echo "Make NICs available for PCI passthrough..."
xl pci-assignable-add 02:00.0
xl pci-assignable-add 03:00.0
xl pci-assignable-add 04:00.0

echo "Creating 1st NDVM..."
xl create /home/root/hvm-conf/ndvm-1.cfg

echo "Creating 2nd NDVM..."
xl create /home/root/hvm-conf/ndvm-2.cfg

echo "Creating 3rd NDVM..."
xl create /home/root/hvm-conf/ndvm-3.cfg

sleep 90

echo "Creating Firewall VM..."
xl create /home/root/hvm-conf/pfsense.cfg
