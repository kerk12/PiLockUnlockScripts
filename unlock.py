import serial
from time import sleep

def unlock():
    ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600)
    ser.isOpen()
    sleep(2)  # Wait for the arduino to be ready.
    ser.write(b"ENABLE")
    ser.close()

if __name__ == "__main__":
    unlock()