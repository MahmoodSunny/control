# pi_control.service will need to be copied to /lib/systemd/system/:
sudo cp pi_control.service /lib/systemd/system/

# enable on boot:
sudo systemctl enable pi_control.service


