# Testing code for Motor_Controller class implementation
# verify functionality is working
from motor_controller import Motor_Controller
import time

# Define motor1 pins
left1 = 23
right1 = 22
channel1 = 0

# Define motor2 pins
left2 = 27
right2 = 17
channel2 = 1

# start the motor controller
motors = Motor_Controller(left1, right1, left2, right2, channel1, channel2)

# test left motor
print("left motor increment forward")
i = 0
while i <= 1000:
    motors.motor1(i/1000)
    time.sleep(0.002)
    i += 1
i = 1000
while i >= 0:
    motors.motor1(i/1000)
    time.sleep(0.002)
    i -= 1
print("left motor increment reverse")
i = 0
while i <= 1000:
    motors.motor1(-i/1000)
    time.sleep(0.002)
    i += 1
i = 1000
while i >= 0:
    motors.motor1(-i/1000)
    time.sleep(0.002)
    i -= 1

# test right motor
print("right motor increment forward")
i = 0
while i <= 1000:
    motors.motor2(i/1000)
    time.sleep(0.002)
    i += 1
i = 1000
while i >= 0:
    motors.motor2(i/1000)
    time.sleep(0.002)
    i -= 1
print("right motor increment reverse")
i = 0
while i <= 1000:
    motors.motor2(-i/1000)
    time.sleep(0.002)
    i += 1
i = 1000
while i >= 0:
    motors.motor2(-i/1000)
    time.sleep(0.002)
    i -= 1

# cleanup GPIO
motors.cleanup()

