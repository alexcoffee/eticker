#!/usr/bin/env bash

P23=""
while [ "$P23" = "" ]; do
   P23=$(whiptail --title "Please select Python version"  --menu  "" 12 50 4 \
   " 2"  "Python 2 (default) " \
   " 3"  "Python 3           " \
   "23"  "Python 2 and 3     "  3>&1 1>&2 2>&3)
   if [ $? = 1 ]; then
      whiptail --msgbox "No version selected. Try again" 8 40
   fi
done
PY2=0
PY3=0
if [[ "$P23" == *"2"* ]]; then
   PY2=1
fi
if [[ "$P23" == *"3"* ]]; then
   PY3=1
fi

# Install required packages
apt-get install git bc i2c-tools fonts-freefont-ttf whiptail make gcc -y
if [ $PY2 -eq 1 ]; then
   apt-get install python-pil python-smbus python-dateutil -y
fi
if [ $PY3 -eq 1 ]; then
   apt-get install python3-pil python3-smbus python3-dateutil -y
fi

# Enable SPI and I2C
raspi-config nonint do_spi 0
raspi-config nonint do_i2c 0

git clone --depth=1 https://github.com/PiSupply/PaPiRus.git
cd PaPiRus

# Install Papirus Python library for Python 2 and/or 3
if [ $PY2 -eq 1 ]; then
   python setup.py install
fi
if [ $PY3 -eq 1 ]; then
   python3 setup.py install
fi

# Install drivers and setup epaper
papirus-setup

whiptail --msgbox "The system will now reboot" 8 40
reboot