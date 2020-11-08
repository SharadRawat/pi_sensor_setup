import serial

ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0,1]
while True:
    read_serial=ser.readline().strip()
    values = read_serial.decode('ascii').split(',')
    a = [float(s) for s in values]
    print(a)
