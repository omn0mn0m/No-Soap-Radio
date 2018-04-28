# Update Pi
sudo apt-get update
sudo apt-get upgrade

# Install RTL-SDR
sudo apt-get install rtl-sdr

# Hardware changes
echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
sudo reboot