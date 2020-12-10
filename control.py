
load_pin = 23
switch_pin = 24

class Control(object):
    """Raspberry Pi 'Control'."""

    def __init__(self):
        pass
    def read_switch(self):
        """Read the state of the switch, and return it (as a boolean)"""
        switch_state = True
        return switch_state
        pass
    def set_load(self, value):
        """Change the load to the passed in value, either True for ON or False for OFF"""
        return 0
        pass