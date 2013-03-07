import threading
import RPi.GPIO as GPIO
import time

class Info:
	@staticmethod
	def p(message):
		print 'Info: '+message 
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
		GPIO.output(self.pin[0],True)
		GPIO.output(self.pin[1],False)
	def stop(self):
		GPIO.output(self.pin[0],False)
		GPIO.output(self.pin[1],False)
	def back(self):
		Info.p('wheel ' +self.name + ' is backing')
		GPIO.output(self.pin[0],False)
		GPIO.output(self.pin[1],True)
		
		
class Car:
	#wheel=[Wheel('a'),Wheel('b'),Wheel('c'),Wheel('d')] 
	wheel=[Wheel('a'),Wheel('b'),Wheel('c'),Wheel('d')] 
	far = Detector(11)
	@staticmethod
	def init():
		GPIO.setmode(GPIO.BOARD)
		Info.p('initialize the smart car ....')		
		Info.p('Smart car is ready to fly!')
		Car.far.start()
	@staticmethod
	def forward():
		Info.p('go straight forward')
		for wheel in Car.wheel:
			wheel.forward()
	@staticmethod
	def fleft():
		Info.p('turn left ')
		Car.wheel[0].forward()	
		Car.wheel[1].forward()
		Car.wheel[3].back()
		Car.wheel[2].back()
	@staticmethod
	def fright():
		Info.p('turn left ')
		Car.wheel[1].forward()	
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
	try:
		Car.init()
		def handler():
			print 'found something'
			Car.stop()
		Car.far.addhandler(handler)
		#Car.fleft()
		#time.sleep(4)
		#Car.bright()
        	#Car.forward()
		time.sleep(2)
		#Car.back()
		time.sleep(2)
		#Car.fright()
		#time.sleep(2)
		#Car.fleft()
		#time.sleep(2)
		#Car.bleft()
		#time.sleep(2)
		#Car.bright()
		#time.sleep(2)
 		#Car.stop()
	except:  
		print 'Error occured'
		import traceback
		traceback.print_exc()
	else:
		GPIO.cleanup()


car_example()
