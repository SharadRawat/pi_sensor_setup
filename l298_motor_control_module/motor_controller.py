import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)



def forward(sec):
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(sec)
    gpio.cleanup()
    
    
def reverse(sec):
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(sec)
    gpio.cleanup()
    

def left_turn(sec):
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(sec)
    gpio.cleanup()
    
def forward_right_turn(sec):
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, True)
    time.sleep(sec)
    gpio.cleanup()  

    
    
seconds = 2

time.sleep(seconds)
print("forward")
forward(seconds-1)
time.sleep(seconds-1)

#forward_right_turn(seconds-4)

reverse(seconds-1)


#forward_right_turn(seconds-4.5)
print("reverse")
#reverse(seconds-4)
#time.sleep(seconds-4.5)
'''
print("left_turn")
left_turn(seconds)
time.sleep(seconds)


print("right_turn")
forward_right_turn(seconds-2)
forward(seconds)
time.sleep(seconds)
'''

### TODO Map the time with how much should the robot rotate