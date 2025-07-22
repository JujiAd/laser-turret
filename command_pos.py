#!/usr/bin/python

# Pi Nerf Turret Controller using pynput
import argparse
from adafruit_servokit import ServoKit

# Initialize parser
msg = "CLI tool for commanding servos to specific position"
parser = argparse.ArgumentParser(description = msg)
parser.add_argument("-x","--x_pos",help="x position (0 to 180)")
parser.add_argument("-y","--y_pos",help="x position (0 to 180)")
args = parser.parse_args()

# Define object for servo control
kit = ServoKit(channels=16)

# Pins of each servo
x_axis = 12
trigger = 13
y_axis = 14

if args.y_pos: kit.servo[y_axis].angle = int(args.y_pos)
if args.x_pos: kit.servo[x_axis].angle = int(args.x_pos)
