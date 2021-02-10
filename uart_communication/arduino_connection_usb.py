import serial
import statistics

ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0,1]
b = []
count = 0
while True:
    count += 1
    read_serial=ser.readline().strip()
    values = read_serial.decode('ascii').split(',')
    a = [float(s) for s in values]
    b += a
    print(statistics.mean(b))
