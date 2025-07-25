#!/usr/bin/python

# Pi Nerf Turret Controller using pynput

import time
from adafruit_servokit import ServoKit


# Define object for servo control
kit = ServoKit(channels=16)

# Pins of each servo
x_axis = 12
trigger = 13
y_axis = 14

# Position Variables
y_position = 100
x_position = 90
trigger_position = 0

# Limits
y_max = 180
y_min = 30
x_max = 180
x_min = 0
trigger_min = 0
y_increment_unit = 1
x_increment_unit = 1

# State
pressed_keys = set()
running = True


def reset_defaults():
    kit.servo[y_axis].angle = 50
    kit.servo[trigger].angle = trigger_min
    kit.continuous_servo[x_axis].throttle = 0
    
wait = 0.05
def y_rom():
    # start from min
    kit.servo[y_axis].angle = y_min
    time.sleep(wait)
    
    for i in range(y_min, y_max):
        time.sleep(wait)
        kit.servo[y_axis].angle = i
        print(f"Y: {i}")
        
    for i in range(y_max, y_min, -1):
        time.sleep(wait)
        kit.servo[y_axis].angle = i
        print(f"Y: {i}")
        
def x_rom():
    # start from min
    kit.servo[x_axis].angle = y_min
    time.sleep(wait)
    
    for i in range(x_min, x_max):
        time.sleep(wait)
        kit.servo[x_axis].angle = i
        print(f"Y: {i}")
        
    for i in range(x_max, x_min, -1):
        time.sleep(wait)
        kit.servo[x_axis].angle = i
        print(f"Y: {i}")
   
# Main control loop
def control_loop():
    global x_position, y_position, running

    kit.servo[y_axis].angle = y_position

    while running:
        time.sleep(0.01)

        if 'w' in pressed_keys:
            y_position += y_increment_unit
            if y_position <= y_max:
                kit.servo[y_axis].angle = y_position
                print(f"Y: {y_position}")
            else:
                y_position -= y_increment_unit

        if 's' in pressed_keys:
            y_position -= y_increment_unit
            if y_position >= y_min:
                kit.servo[y_axis].angle = y_position
                print(f"Y: {y_position}")
            else:
                y_position += y_increment_unit

        if 'a' in pressed_keys:
            x_position -= x_increment_unit
            if x_position >= x_min:
                kit.servo[x_axis].angle = x_position
                print(f"X: {x_position}")
            else:
                x_position += x_increment_unit

        if 'd' in pressed_keys:
            x_position += x_increment_unit
            if x_position <= x_max:
                kit.servo[x_axis].angle = x_position
                print(f"X: {x_position}")
            else:
                x_position -= x_increment_unit

        if 'space' in pressed_keys:
            print("Firing!")
            kit.servo[trigger].angle = 100
            time.sleep(0.3)
            kit.servo[trigger].angle = 0
            pressed_keys.discard('space')  # prevent repeat firing

        if 'q' in pressed_keys:
            print("Quitting...")
            kit.servo[y_axis].angle = 80
            running = False
            break
        
if __name__ == "__main__":
    # y_rom()
    x_rom()
