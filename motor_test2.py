# Testing code for Motor_Controller class implementation
# verify functionality is working
from motor_controller import Motor_Controller
import time
from getkey import getkey, keys

print("WELCOME TO IKEA BOT 3000 MANUAL MOTOR CONTROL")
print("PRESS w/s KEYS FOR LEFT MOTOR FORWARD REVERSE")
print("PRESS up/down KEYS FOR RIGHT MOTOR FORWARD REVERSE")
print("PRESS ANY OTHER KEY TO CLOSE OUT")

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

left_motor_speed = 0
right_motor_speed = 0

def print_speed():
    print(left_motor_speed/10, right_motor_speed/10)

while True:
    key = getkey()
    if key == keys.UP:
        right_motor_speed += 1
        print_speed()
    elif key == keys.DOWN:
        right_motor_speed -= 1
        print_speed()

    elif key == "w":
        left_motor_speed += 1
        print_speed()
    elif key == "s":
        left_motor_speed -= 1
        print_speed()

    else:
        print("bye")
        break

    motors.motor1(left_motor_speed/10)
    motors.motor2(right_motor_speed/10)
    
# cleanup GPIO
motors.cleanup()

