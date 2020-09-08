#!user/bin/python3

from mpu6050 import mpu6050
sensor = mpu6050(0x68)

while (1):
    accelerometer_data = sensor.get_accel_data()
    temp = sensor.get_temp()
    gyro_data = sensor.get_gyro_data()
    
    print("Acceleration")
    print("-----------------")
    print(accelerometer_data)
    
    print("-----------------")
    print("Temperatue")
    print("-----------------")
    print(temp)
    
    print("-----------------")
    print("Gyro data")
    print("-----------------")
    print(gyro_data)
    print("-----------------")
    
