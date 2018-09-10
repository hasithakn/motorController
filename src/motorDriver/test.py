#from gpiozero import PWMOutputDevice
import RPi.GPIO as GPIO
from time import sleep
import MotorLib as m

def main():
	m.motorL(0,55)
	sleep(2);
	m.motorL(1,100)
	sleep(2)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
