#from gpiozero import PWMOutputDevice
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

speedLeftPin=21
PWM_FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive


speedRightPin=5
PWM_FORWARD_RIGHT_PIN = 13	# IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive
 

GPIO.setup(speedLeftPin, GPIO.OUT) # Connected to PWMA
GPIO.setup(PWM_FORWARD_LEFT_PIN, GPIO.OUT) # Connected to AIN2
GPIO.setup(PWM_REVERSE_LEFT_PIN, GPIO.OUT) # Connected to AIN1

GPIO.setup(speedRightPin, GPIO.OUT) # Connected to PWMA
GPIO.setup(PWM_FORWARD_RIGHT_PIN, GPIO.OUT) # Connected to AIN2
GPIO.setup(PWM_REVERSE_RIGHT_PIN, GPIO.OUT) # Connected to AIN1

speedL = GPIO.PWM(speedLeftPin, 1000)
speedR = GPIO.PWM(speedRightPin, 1000)

def motorL(func,data):
	if(func==0):
		speedL.start(data)
		GPIO.output(PWM_FORWARD_LEFT_PIN, GPIO.LOW)
		GPIO.output(PWM_REVERSE_LEFT_PIN, GPIO.HIGH)
	elif(func==1):
		speedL.start(data)
		GPIO.output(PWM_FORWARD_LEFT_PIN, GPIO.HIGH)
		GPIO.output(PWM_REVERSE_LEFT_PIN, GPIO.LOW)

def motorR(func,data):
	if(func==0):
		speedR.start(data)
		GPIO.output(PWM_FORWARD_RIGHT_PIN, GPIO.LOW)
		GPIO.output(PWM_REVERSE_RIGHT_PIN, GPIO.HIGH)
	elif(func==1):
		speedR.start(data)
		GPIO.output(PWM_FORWARD_RIGHT_PIN, GPIO.HIGH)
		GPIO.output(PWM_REVERSE_RIGHT_PIN, GPIO.LOW)




# def main():
# 	motorL(0,55)
# 	sleep(5);
# 	motorL(1,55)
#
# if __name__ == "__main__":
#     """ This is executed when run from the command line """
#     main()
