import serial
from time import sleep
ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600)
ser.isOpen()
sleep(2)  # Wait for the arduino to be ready.
ser.write("ENABLE")
ser.close()
exit()
