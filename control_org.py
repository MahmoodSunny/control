import RPi.GPIO as GPIO

load_pin = 23
switch_pin = 24

class Control(object):
    """Raspberry Pi 'Control'."""

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) # Using BCM convention to identify GPIO pins
        GPIO.setup(load_pin, GPIO.OUT) # Load connected to pin 23, as output
        GPIO.setup(switch_pin, GPIO.IN) # switch connected to pin 24, as input
        pass
    def read_switch(self):
        """Read the state of the switch, and return it (as a boolean)"""
        return GPIO.input(switch_pin)
        pass
    def set_load(self, value):
        """Change the load to the passed in value, either True for ON or False for OFF"""
        return GPIO.output(load_pin, value)
        pass