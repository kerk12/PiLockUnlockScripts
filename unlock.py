import serial

ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600)

ser.write("ENABLE")
ser.close()
exit()