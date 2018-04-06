import serial
from time import sleep
import RPi.GPIO as GPIO

# Mode switch
# 0 -> GPIO Unlock
# 1 -> Arduino Assisted Unlock (default before 0.3.1)
MODE = 0
# The GPIO pin used for the switch. Refer to your RPi's PinOut diagram.
# Used only when MODE = 0 
SW_PIN = 18 

def unlock():
    if MODE == 0:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(SW_PIN, GPIO.OUT)
        GPIO.output(SW_PIN, GPIO.HIGH)
        sleep(5)
        GPIO.output(SW_PIN, GPIO.LOW)
        GPIO.cleanup()
    else:
        ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600)
        ser.isOpen()
        sleep(2)  # Wait for the arduino to be ready.
        ser.write(b"ENABLE")
        ser.close()

if __name__ == "__main__":
    unlock()
