# kennedyengineering 2020

import RPi.GPIO as GPIO
import Adafruit_PCA9685
# use BCM numbering
GPIO.setmode(GPIO.BCM)

class H_Bridge:
    def __init__(self, left: int, right: int):
        # save pin configuration
        self.GPIO_left = left
        self.GPIO_right = right
        
        # make the pins outputs
        GPIO.setup(self.GPIO_left,  GPIO.OUT)
        GPIO.setup(self.GPIO_right, GPIO.OUT)

        # make sure motor is stopped
        self.stop()

    def stop(self):
        # stop motor, pull pins low
        GPIO.output(self.GPIO_left, GPIO.LOW)
        GPIO.output(self.GPIO_right, GPIO.LOW)

    def left(self):
        # stop motor before switching, prevent shorting
        self.stop()
        # pull left pin high
        GPIO.output(self.GPIO_left, GPIO.HIGH)
        GPIO.output(self.GPIO_right, GPIO.LOW)
    
    def right(self):
        # stop motor before switching, prevent shorting
        self.stop()
        # pull right pin high
        GPIO.output(self.GPIO_left, GPIO.LOW)
        GPIO.output(self.GPIO_right, GPIO.HIGH)

    def cleanup(self):
        # clean up used channels
        self.stop()
        GPIO.cleanup(self.GPIO_left)
        GPIO.cleanup(self.GPIO_right)


class Motor_Controller:
    def __init__(self, left1, right1, left2, right2, channel1, channel2):
        # configure H_BRIDGE
        self.h_bridge1 = H_Bridge(left1, right1)
        self.h_bridge2 = H_Bridge(left2, right2)
        
        # configure PCA9685
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.duty_cycle = 4095
        self.pwm_freq = 100 #Hz between 40 & 1000
        self.channel1 = channel1
        self.channel2 = channel2
        self.pwm.set_pwm_freq(self.pwm_freq)

        self.motor1(0)
        self.motor2(0)

    def motor1(self, power):
        # power is float from -1 -> 1
        # determines direction and PWM frequency
        power = max(-1.0, min(1.0, power))
        pwm = int(self.duty_cycle * abs(power))
        
        if power < 0:
            # negative power, turn motor left
            self.h_bridge1.left()
        elif power > 0:
            # positive power, turn motor right
            self.h_bridge1.right()
        else:
            # zero power, stop motor
            self.h_bridge1.stop()

        self.pwm.set_pwm(self.channel1, 0, pwm)

    def motor2(self, power):
        # power is float from -1 -> 1
        # determines direction and PWM frequency
        power = max(-1.0, min(1.0, power))
        pwm = int(self.duty_cycle * abs(power))
        
        if power < 0:
            # negative power, turn motor left
            self.h_bridge2.left()
        elif power > 0:
            # positive power, turn motor right
            self.h_bridge2.right()
        else:
            # zero power, stop motor
            self.h_bridge2.stop()

        self.pwm.set_pwm(self.channel2, 0, pwm)

    def cleanup(self):
        self.motor1(0)
        self.motor2(0)
        self.h_bridge1.cleanup()
        self.h_bridge2.cleanup()

