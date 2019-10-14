# WARNING

This is WIP repo and it is under development. Use it at your own risk. 
If you have use-cases for such thing to be developed, please submit
an issue or PR with description of your needs / fixes.

# meta-pcengines

Yocto BSP layer for PC Engines hardware

# Building

```
SHELL=bash kas-docker --ssh-dir ~/ssh-keys build meta-pcengines/kas.yml
```
# Flashing drive with dd 

Check a directory of the drive to be flash using the command:

```
sudo fdisk -l
``` 

Change directory to  <build-directory>/tmp/deploy/images/pcengines-apu2 and flash the drive:

```
sudo dd if=xen-dom0-image-pcengines-apu2.hddimg of=/dev/<drive_dir>
```

# Bootup log

The bootup log [example](#).  
