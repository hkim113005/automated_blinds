import RPi.GPIO as GPIO
import time
from RpiMotorLib import RpiMotorLib

GPIO_pins = (14, 15, 18)
direction= 20
step = 21

motor = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "DRV8825")

def up(v):
    motor.motor_go(False, "Full" , v, .002, False, .01)
    
def down(v):
    motor.motor_go(True, "Full", v, .002, False, .01)


GPIO.cleanup()
