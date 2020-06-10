#!user/bin/python3

from mpu6050 import mpu6050
sensor = mpu6050(0x68)

while (1):
    accelerometer_data = sensor.get_accel_data()
    temp = sensor.get_temp()
    gyro_data = sensor.get_gyro_data()
    print(accelerometer_data)
    print(temp)
    print(gyro_data)
    
