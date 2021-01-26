import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(13, gpio.OUT)



def forward_slow(sec):
    init()
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=40
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)

    
    time.sleep(sec)
    pwm17.stop(t)
    pwm22.stop(t)
    gpio.cleanup()

def forward_faster(sec):
    init()
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=75
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)

    
    time.sleep(sec)
    pwm17.stop(t)
    pwm22.stop(t)
    gpio.cleanup()

def forward_fastest(sec):
    init()
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=100
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)

    
    time.sleep(sec)
    pwm17.stop(t)
    pwm22.stop(t)
    gpio.cleanup()
    
def reverse(sec):
    init()
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=100
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(sec)
    gpio.cleanup()
    

def left_turn(sec):
    init()
    
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=100
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(sec)
    gpio.cleanup()
    
def forward_right_turn(sec):
    
    init()
    pwm17 = gpio.PWM(12,100)
    pwm22 = gpio.PWM(13,100)
    t=100
    pwm17.start(t)
    pwm22.start(t)
    
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, True)
    time.sleep(sec)
    gpio.cleanup()  

    
    
seconds = 1



#forward(seconds-1)

#reverse(seconds-1)
print("forward")

print("forward and right")
forward_right_turn(seconds)

forward_right_turn(seconds)

forward_right_turn(seconds)

forward_right_turn(seconds)
#forward_faster(seconds+3)
#forward_fastest(seconds+3)
time.sleep(1)

#forward_right_turn(seconds-4)

#reverse(seconds-1)


#forward(seconds+1)
#print("reverse")
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