do_install_append() {
    # set hardware watchdog timeout to 60 seconds
    sed -e  's/.*RuntimeWatchdogSec=.*/RuntimeWatchdogSec=60/' -i ${D}${sysconfdir}/systemd/system.conf
}
