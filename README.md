# WARNING

This is WIP repo is under development. Use it at your own risk.
If you have use-cases for such thing to be developed, please submit
an issue or PR with description of your needs / fixes.

# meta-pcengines

Yocto BSP layer for PC Engines hardware

# Building

Make sure to adjust `~/ssh-keys` according to your configuration:

```
SHELL=bash kas-docker --ssh-dir ~/ssh-keys build meta-pcengines/kas-docker.yml
```

Check a device node of the drive to be flashed:

```
sudo fdisk -l
```

Change directory to `<build-directory>/tmp/deploy/images/pcengines-apu2`. Find
desired image and flash the drive:

```
sudo dd if=xen-dom0-image-pcengines-apu2.hddimg of=/dev/<drive_dir>
```

# Bootup log

The bootup log [example](bootup.log).

# Issues

If you have any trouble or find any bug, please report an issue in 
[this location](https://github.com/pcengines/apu2-documentation/issues). To 
create the issue, from the list of available templates select the one, that fits 
best the nature of the issue (bug, feature, question or task) and fill it.
