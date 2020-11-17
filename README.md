# WARNING

This is WIP repo is under development. Use it at your own risk.
If you have use-cases for such thing to be developed, please submit
an issue or PR with description of your needs / fixes.

# meta-pcengines

Yocto BSP layer for PC Engines hardware

# Building

```
SHELL=/bin/bash kas-docker build meta-pcengines/kas-docker.yml
```

Check a device node of the drive to be flashed:

```
sudo fdisk -l
```

Change directory to `<build-directory>/tmp/deploy/images/pcengines-apu2`. Find
desired image and flash the drive:

> Replace the `/dev/sdx` with the proper device path

```
sudo bmaptool copy --bmap docker-image-minimal-pcengines-apu2.wic.bmap docker-image-minimal-pcengines-apu2.wic.gz /dev/sdx
```

> The `bmaptool` can flash images much faster than the `dd`

or if `bmap-tools` are not available in your system:

```
gzip -cdk docker-image-minimal-pcengines-apu2.wic.gz | sudo dd of=/dev/sdx
```

# Bootup log

The bootup log [example](bootup.log).
