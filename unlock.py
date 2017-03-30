import serial

ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600)

ser.is_open()

ser.write("ENABLE\0")
ser.close()
exit()