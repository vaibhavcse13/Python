class Stack():
	"""docstring for Stack"""

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self,itm) :
		self.items.append(itm)

	def pop(self):
		return self.items.pop();

	def peek(self):
		return self.items[len(self.items) -1]

	def size(self):
		return len(self.items);




		