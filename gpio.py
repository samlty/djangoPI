#!/usr/bin/python
import sys
import pdb
import RPi.GPIO
import time

class gpio():
    def __init__(self):
	RPi.GPIO.setmode(RPi.GPIO.BCM) 
        RPi.GPIO.setwarnings(False)
        self.__left_up_1=17
        self.__left_up_2=18
        self.__left_down_1=27
        self.__left_down_2=22
        self.__right_up_1=23
        self.__right_up_2=24
        self.__right_down_1=25
        self.__right_down_2=4

	self.__init_wheel_pin()

    def __init_wheel_pin(self):
	RPi.GPIO.setup(self.__left_up_1,RPi.GPIO.OUT)
	RPi.GPIO.setup(self.__left_up_2,RPi.GPIO.OUT)
	RPi.GPIO.setup(self.__left_down_1,RPi.GPIO.OUT)
	RPi.GPIO.setup(self.__left_down_2,RPi.GPIO.OUT)
	RPi.GPIO.setup(self.__right_up_1,RPi.GPIO.OUT)
	RPi.GPIO.setup(self.__right_up_2,RPi.GPIO.OUT)
	RPi.GPIO.setup(self.__right_down_1,RPi.GPIO.OUT)
	RPi.GPIO.setup(self.__right_down_2,RPi.GPIO.OUT)
    def __left_forward(self):
        print "left forward"
	RPi.GPIO.output(self.__left_up_2,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__left_up_1,RPi.GPIO.LOW)
	RPi.GPIO.output(self.__left_down_1,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__left_down_2,RPi.GPIO.LOW)
    def __left_backward(self):
	RPi.GPIO.output(self.__left_up_1,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__left_up_2,RPi.GPIO.LOW)
	RPi.GPIO.output(self.__left_down_2,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__left_down_1,RPi.GPIO.LOW)
        
    def __left_stop(self):
        print "left stop"
	RPi.GPIO.output(self.__left_up_1,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__left_up_2,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__left_down_2,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__left_down_1,RPi.GPIO.HIGH)




    def __right_forward(self):
        print "right forward"
	RPi.GPIO.output(self.__right_up_2,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__right_up_1,RPi.GPIO.LOW)
	RPi.GPIO.output(self.__right_down_2,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__right_down_1,RPi.GPIO.LOW)
	
    def __right_backward(self):
	RPi.GPIO.output(self.__right_up_1,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__right_up_2,RPi.GPIO.LOW)
	RPi.GPIO.output(self.__right_down_1,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__right_down_2,RPi.GPIO.LOW)

    def __right_stop(self):
        print "right stop"
	RPi.GPIO.output(self.__right_up_1,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__right_up_2,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__right_down_1,RPi.GPIO.HIGH)
	RPi.GPIO.output(self.__right_down_2,RPi.GPIO.HIGH)




    def forward(self):

	self.__left_forward()
	self.__right_forward()
    def backward(self):

	self.__left_backward()
	self.__right_backward()
    def turn_left(self):
        self.__right_forward()
        self.__left_stop()
    def turn_right(self):
        self.__left_forward()
        self.__right_stop()
    def stop(self):
        self.__left_stop()
        self.__right_stop()
if __name__ == '__main__':
    #pdb.set_trace()
    gpio = gpio()
    if len(sys.argv) < 2:
        print("need add parameter as:")
        print(" l -- as turn left")
        print(" r -- as turn right")
        print(" f -- as forward")
        print(" b -- as backward")
        print(" s -- as stop")

    else:
        cmd = sys.argv[1]
        if 'l' == cmd.lower():
            print "cmd turn left"
            gpio.turn_left()    
        elif 'r' == cmd.lower():
            gpio.turn_right()    

        elif 'f' == cmd.lower():
            gpio.forward()    
        elif 'b' == cmd.lower():
            gpio.backward()    
        elif 's' == cmd.lower():
            gpio.stop()    
        else:
            gpio.forward()    
          
