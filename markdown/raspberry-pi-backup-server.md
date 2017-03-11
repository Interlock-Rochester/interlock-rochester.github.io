Raspberry Pi Backup Server
==========================

date
:   2016-09-20 20:26

author
:   carl

category
:   Uncategorized

slug
:   raspberry-pi-backup-server

status
:   published

Last week I presented on How Do I Make a backup server with a
raspberrypi. I covered going from a fresh pi to working network drive in
probably about 30 minutes of actual work along with 30 minutes of
talking about options for other things to do. There were 6 or so people
that came and for those people, and others that could not make it, here
are my notes on how to do this. It is not a recipe file with step by
step with commands that can be cut and pasted. This is because there are
lots of options and the values I use are going to be different that what
you will need on your network. These instructions will guide you through
this and tell you where to get things.

Buy raspi 2 or 3, hard drive(s), case(s), sd card\
Download Raspian - <https://www.raspberrypi.org/downloads/raspbian/>\
Write image to sd card -
<https://www.raspberrypi.org/documentation/installation/installing-images/README.md>\
connect keyboard and network to raspi

Boot raspi\
login: pi password: raspberry

edit /etc/default/keyboard, change gb to us, save and reboot

apt-get update\
apt-get upgrade

useradd to create the network backup owner\
ssh-keygen to make .ssh and some keys\
edit \~netback/.ssh/authorized\_keys to add your keys

apt-get install samba samba-common-bin nfs-common nfs-server rsync

parted to check partitions on USB disks\
mkfs to create the file systems\
edit /etc/fstab to mount the USB drives

<http://theurbanpenguin.com/wp/index.php/setting-up-a-samba-server-on-raspberry-pi/>

edit /etc/samba/smb.conf\
start nmbd and smbd\
smbpasswd -a netback\
edit /etc/exports\
exportfs\
update the nfs-kernel-server files\
start service\
Use rsync from linux or mac to backup to the raspi\
\#!/bin/bash

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

if [ "X\$1" == "X" ]; then\
echo "Missing argument"\
echo "Usage: \$0 {1|2}"\
exit 1\
fi

DAY=\`date +%d\`\
DESTDIR=/back\$1\
BACKDIR=/back\$1/backup/day.\$DAY\
SRCDIR=/home\
LOGFILE=/var/log/sync\$1/log.\$DAY

if [ -d \$BACKDIR ]; then\
rm -rf \$BACKDIR\
fi

mkdir \$BACKDIR\
cd \$DESTDIR

time rsync -avHb --backup-dir=\$BACKDIR --delete 172.16.100.10:\$SRCDIR
. \> \$LOGFILE 2\>&1

tail -30 \$LOGFILE | Mail -s "rasp01 nightly sync \$1 of colossus"
<cws@faultline.com>

exit 0
