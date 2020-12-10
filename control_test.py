from control import Control

# Create an instance of the control class
control = Control()

# Get the current switch state and print it out
switch = control.read_switch()
print('Switch: {0}'.format(switch))

# Blink the load (when it is a LED)
print('Blinking LED')
while True:
    control.set_load(True)
    time.sleep(0.5)
    control.set_load(False)
    time.sleep(0.5)