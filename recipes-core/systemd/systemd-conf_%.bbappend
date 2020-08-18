do_install_append() {
    # set hardware watchdog timeout to 60 seconds
    sed -e  's/.*RuntimeWatchdogSec=.*/RuntimeWatchdogSec=60/' -i ${D}${systemd_unitdir}/system.conf.d/00-${PN}.conf
}
