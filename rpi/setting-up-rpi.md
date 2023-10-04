# RPI Setup 

# Flash RPI OS to SD Card 

### Raspberry Pi now has their own image burning service for when you set it up! Rather than using Etcher
1. Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and follow the directions !!

## SSHing into rpi
1. Insert SD card
1. Connect ethernet to laptop (that’s connected to WiFi)
  - Laptop might need to enable Internet Sharing in settings
1. Connect power to RPI last (give it 1 min to boot)
1. Scan for rpi on network (should be raspberrypi.local): `arp-a   // or ifconfig`
1. SSH: `ssh pi@raspberrypi.local // ѕѕh pi@192.168.2.2`
1. If needed, download lxsession/Vim/Chromium
1. SSH with -X and lxsession for GUI: `ѕѕh -X pi@192.168.2.2 lxѕеѕѕіоn`
1. Test for internet access: `ping www.google.com`

## Connecting via Wifi

1. `sudo raspi-config` > `System Options` > `Wireless LAN` > enter wifi info 

Shoutout to @anyu for the help on this one :))
