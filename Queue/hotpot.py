import myQueue 

def hotPotato(namelist , num ):
	qu = myQueue.Queue()

	for name in namelist :
		qu.enqueue(name)

	while qu.size() > 1 :

		for i in range(num):
			qu.enqueue(qu.dequeue())

		qu.dequeue()

	return qu.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))