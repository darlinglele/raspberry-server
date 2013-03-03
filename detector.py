import threading
import RPi.GPIO as GPIO
import time
class Detector:
	def __init__(self, pin):
		self.pin = pin
		self.handlerlist=[]
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.IN)
		Info.p('init a detector on pin '+str(pin))
	def start(self):
		Info.p ('detector is listening on pin'+str(self.pin))
		t = threading.Thread(target = self.run)
		t.daemon = True 
		t.start()

	def destory(self):
		Info.p ('destroy the detector')
	
	def run(self):
		while True:
			if GPIO.input(self.pin) is False:
				for handler in self.handlerlist:
					handler()
	def addhandler(self,handler):
		self.handlerlist.append(handler)

class Wheel:
	pins ={'a':13,'b':15,'c':16,'d':18}
	def __init__(self,name):
		self.name = name
		self.pin = Wheel.pins[self.name]
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin,GPIO.OUT)
	def go(self):
		Info.p('wheel ' + self.name + ' is runing')
		GPIO.output(self.pin,True)
	def stop(self):	
		Info.p('wheel ' + self.name + ' is stoping')
		GPIO.output(self.pin, False)
		
class Car:
	wheel=[Wheel('a'),Wheel('b'),Wheel('c'),Wheel('d')] 

	@staticmethod
	def init():
		Info.p('initialize the smart car ....')		
		Info.p('Smart car is ready to fly!')

	@staticmethod
	def forward():
		Info.p('go straight forward')
		for wheel in Car.wheel:
			wheel.go()

	@staticmethod
	def back():
		Info.p('go straight back')

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


class Info:
	@staticmethod
	def p(message):
		print 'Info: '+message 

def followthing():
	print 'following the target...';
def stop():
	print 'too close to target,stopping ....';
def Detecter_example():
	far = Detector(11)
	far.addhandler(followthing)
	far.start();
	near = Detector(12)
	near.start()
	near.addhandler(stop)
	time.sleep(5)
	far.addhandler(stop)
	time.sleep(20)
	far.destory()
	near.destory()
def car_example():
	Car.forward()
	Car.stop()


car_example()
