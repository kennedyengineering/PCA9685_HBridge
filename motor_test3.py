# Manual operation of motor controller test application
from motor_controller import Motor_Controller
from getkey import getkey, keys
import os

welcome_message = \
"""
WELCOME TO THE IKEA BOT 3000 MANUAL MOTOR CONTROL PROGRAM
PRESS w/s TO INCREASE AND DECREASE MOTOR SPEED
PRESS a/d TO TURN LEFT OR RIGHT
PRESS ANY OTHER KEY TO CLOSE OUT
"""

rows, columns = os.popen('stty size', 'r').read().split()
char_width = int(columns)

def print_welcome():
    for line in welcome_message.splitlines():
        print(line.center(char_width, ' '))

print_welcome()

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

speed = 0
bank = 0    # additional speed to left or right motor for turning

def print_speed():
    print(chr(27) + "[2J")  # clear screen
    print_welcome()
    print("\n\n")

    left_speed = (speed/10) - (bank/10)
    right_speed = (speed/10) + (bank/10)

    head = "BANK LEFT\tSPEED\tBANK RIGHT"
    fmt = "{}\t{}\t{}".format(abs(bank/10) if bank < 0 else 0, speed/10, bank/10 if bank > 0 else 0)
    print(head.center(char_width, ' '))
    print(fmt.center(char_width, ' '))
    print("\n")

    head = "LEFT MOTOR\t\tRIGHT MOTOR"
    fmt = "{}\t\t{}".format(left_speed, right_speed)
    print(head.center(char_width, ' '))
    print(fmt.center(char_width, ' '))

    update_motors(left_speed, right_speed)

def update_motors(speed1, speed2):
    motors.motor1(speed1)
    motors.motor2(speed2)

while True:
    key = getkey()

    if key == "w":
        speed += 1
        print_speed()
    
    elif key == "s":
        speed -= 1
        print_speed()
    
    elif key == "a":
        bank -= 1
        print_speed()
    
    elif key == "d":
        bank += 1
        print_speed()

    else:
        print("bye")
        break
    
# cleanup GPIO
motors.cleanup()

