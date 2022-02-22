#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from linerider_lib.linerider import Robot
import rospy
import math
import time

from std_msgs.msg import Float32

robot = Robot("linerider")

#the code starts here

while (robot.is_ok()):
    sensorRow = robot.get_sensor_data()
    max = 0
    index = 0
    for i in range(0, len(sensorRow)):
        if sensorRow[i] > max:
            max = sensorRow[1]
            index = i
            print(i)
    error = (len(sensorRow) / 2) - index
    gain = 0.1
    command = gain*error
    if index <= command/2:
        robot.move(-0.9)
        robot.rotate(command)
    elif index > command/2:
        robot.move(1.7)
        robot.rotate(command)
    else:
        robot.rotate(0.0)

