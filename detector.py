class Detector:
	def __init__(self, pin):
		self.pin = pin
		Info.p('init a detector on pin '+str(pin))
	def start(self):
		Info.p ('detector is listening on pin'+str(self.pin))

	def kill(self):
		Info.p ('kill the detector')

	def onfound(self,eventhandler):
		dosomething()

	def printf(self):
		Info.p ('Somthing was find dfdfdfd')

class Info:
	@staticmethod
	def p(message):
		print 'Info: '+message 

def run_example():
	detector1 = Detector(11)
	detector1.start()
run_example()
