from threading import Thread, Lock
import time
import logging
import random


logging.basicConfig(level=logging.DEBUG,
	format='%(threadName)-1s %(message)s',
	)

locks = [Lock(), Lock(), Lock(), Lock(), Lock()]

def pick(i):
	if locks[i].acquire() != True:
		locks[i].acquire()
		logging.debug('left fork acquired')
		if locks[i+1].acquire() != True:
			locks[i+1].acquire()
			logging.debug('right fork acquired')
			logging.debug('starts eating')
			time.sleep(5)
			logging.debug('manag kaon')
			locks[i].release()
			locks[i+1].release()
			logging.debug('exits')
		else:
			locks[i].release()
			logging.debug('cant get right fork, dropped left fork')

	else:
		time.sleep(2)
		logging.debug('waiting...')

i=0
A = Thread(name = 'Aristotle', target=pick, args=(i,))
K = Thread(name = 'Kant', target=pick, args=(i,))
B = Thread(name = 'Buddha', target = pick, args=(i,)) 
R = Thread(name = 'Russel', target=pick, args=(i,))
M = Thread(name = 'Marx', target = pick, args=(i,)) 

A.start()
K.start()
B.start()
R.start()
M.start()