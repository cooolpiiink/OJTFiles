from threading import Thread, Lock, Event
import time, random, logging, Queue

logging.basicConfig(level=logging.DEBUG,
	format='%(levelname)s: %(message)s',
	)

q = Queue

brb = Lock()

class bbShop(object):
	Chairs = []

	def __init__(self, barber, numChair):
		self.barber = barber
		self.numChair = numChair

	def openShop(self):
		logging.debug('The shop is now open.')
		work = Thread(target = self.barberReady)
		work.start()

	def barberReady(self):
		brb.acquire()

		if len(self.Chairs) is not 0:
			c = self.Chairs[0]
			del self.Chairs[0]
			brb.release()
			self.barber.startCut(c)
		else:
			brb.release()
			logging.debug('Barber is sleeping')
			barber.sleep()
			logging.debug('Barber is awake!')

	def enterShop(self, customer):
		brb.acquire()
		logging.debug(customer.name + ' entered the shop and checking for vacant seats')

		if len(self.Chairs) == self.numChair:
			logging.debug('waiting room is full, ' + customer.name + ' is leaving.')
			brb.release()
		else:
			logging.debug(customer.name + ' is in the waiting room')
			self.Chairs.append(c)
			brb.release()
			barber.wakeUp()

class Customer(object):
	def __init__(self,name):
		self.name = name

class Barber(object):
	barberEvent = Event()

	def sleep(self):
		self.barberEvent.wait()

	def wakeUp(self):
		self.barberEvent.set()
	
	def startCut(self, customer):
		self.barberEvent.clear()

		logging.debug(customer.name + ' is now with the barber.')
		time.sleep(random.randint(4,10))
		logging.debug(customer.name + ' has a new haircut')

if __name__ == '__main__':
	customers=[]
	customers.append(Customer('Ronald'))
	customers.append(Customer('Pete'))
	customers.append(Customer('Santino'))
	customers.append(Customer('Trint'))
	customers.append(Customer('Mango'))
	customers.append(Customer('Float'))

	barber = Barber()

	bbShop = bbShop(barber, numChair=5)
	bbShop.openShop()

	while len(customers) > 0:
		c = customers.pop()

		bbShop.enterShop(c)	
		time.sleep(random.randint(5,100))

