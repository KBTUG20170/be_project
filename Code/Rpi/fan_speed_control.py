# Control Motor speed using PWM module driven by servo motor

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
global pwm
pwm = GPIO.PWM(18, 50)  # 50 Hz frequency

def set_angle(angle):
	duty_cycle = int((angle-0)/180 * (12-2) + 2) # (2 to 12 PWM) = 0 to 180 degrees
	pwm.ChangeDutyCycle(duty_cycle)

load_sequence = [0,12,24,36,48,60,72,84,96,108,120,132,132,120,108,96,84,72,60,48,36,24,12,0,0,12,24,36,48,60,72,84,96,108,120,132,132,120,108,96,84,72,60,48,36,24,12,0,24,36,48,60,72,84,96,108,120,132,144,156,156,144,132,120,108,96,84,72,60,48,36,24,0,12,24,36,48,60,72,84,96,108,120,132,132,120,108,96,84,72,60,48,36,24,12,0,0,12,24,36,48,60,72,84,96,108,120,132,132,120,108,96,84,72,60,48,36,24,12,0,24,36,48,60,72,84,96,108,120,132,144,156,156,144,132,120,108,96,84,72,60,48,36,24,0,12,24,36,48,60,72,84,96,108,120,132,132,120,108,96,84,72,60,48,36,24,12,0,24,36,48,60,72,84,96,108,120,132,144,156,156,144,132,120,108,96,84,72,60,48,36,24,24,36,48,60,72,84,96,108,120,132,144,156,156,144,132,120,108,96,84,72,60,48,36,24,48,60,72,84,96,108,120,132,144,156,168,180,180,168,156,156,144,132,120,108,96,84,72,60,48]

pwm.start(0)  

for i in load_sequence:
	set_angle(i)
	time.sleep(30) # 30 seconds delay = 2hrs, 5 sec = 1440 readings

pwm.stop()
GPIO.cleanup()
