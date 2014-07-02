import threading
import RPi.GPIO as GPIO
import time

class Info:
	@staticmethod
	def p(message):
		print 'Info: '+message 

#Wheel封装的单个车轮的所有可能操作
class Wheel:
	pins ={'a':[13,15],'b':[16,18],'c':[19,21],'d':[22,24]}
	def __init__(self,name):
		self.name = name
		self.pin = Wheel.pins[self.name]
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin[0],GPIO.OUT)
		GPIO.setup(self.pin[1],GPIO.OUT)
		self.stop()
	def st(self):
		print 'ss'
	def forward(self):
		Info.p('wheel ' + self.name + ' is forwarding')
		GPIO.output(self.pin[0],GPIO.HIGH)
		GPIO.output(self.pin[1],GPIO.LOW)
	def stop(self):
		GPIO.output(self.pin[0],False)
		GPIO.output(self.pin[1],False)
	def back(self):
		Info.p('wheel ' +self.name + ' is backing')
		GPIO.output(self.pin[0],False)
		GPIO.output(self.pin[1],True)
		
#Car组合四个轮子所有可能操作		
class Car:
	wheel=[Wheel('a'),Wheel('b'),Wheel('c'),Wheel('d')] 
	@staticmethod
	def init():
		GPIO.setmode(GPIO.BOARD)
		Info.p('initialize the smart car ....')		
		Info.p('Smart car is ready to fly!')
	@staticmethod
	def forward():
		Info.p('go straight forward')
		for wheel in Car.wheel:
			wheel.forward()
	@staticmethod
	def left():
		Info.p('turn left ')
		Car.wheel[0].forward()	
		Car.wheel[1].forward()
		Car.wheel[3].back()
		Car.wheel[2].back()
	@staticmethod
	def right():
		Info.p('turn left ')
		Car.wheel[2].forward()	
		Car.wheel[3].forward()
		Car.wheel[0].back()
		Car.wheel[1].back()
	@staticmethod
	def bleft():
		Info.p('turn left ')
		Car.wheel[2].back()	
	@staticmethod
	def bright():
		Info.p('turn left ')
		Car.wheel[0].back()	
		Car.wheel[1].back()	
		Car.wheel[3].forward()
		Car.wheel[2].forward()
	@staticmethod
	def stop():
		Info.p('turn left ')
		Car.wheel[0].stop()	
		Car.wheel[1].stop()	
		Car.wheel[3].stop()
		Car.wheel[2].stop()
	@staticmethod
	def back():
		Info.p('go straight back')
		for wheel in Car.wheel:
			wheel.back()

	@staticmethod
	def lforward():
		Info.p('go forward and turn left')

	@staticmethod
	def rforward():
		Info.p('go forward and turn right')

	@staticmethod
	def lback():
		Info.p('go back and turn left')

	@staticmethod
	def rback():
		Info.p('go back and turn right')
	@staticmethod
	def stop():
		Info.p('try to stop the car ...')
		for wheel in Car.wheel:
			wheel.stop()	
	@staticmethod
	def bark():
		Info.p('try to slow down the car ...')
	
	@staticmethod
	def speedup():
		Info.p('try to speed up the car ...')

if __name__ =='__main__':
	print '....'
	
