import myStack

def matches(o, c):
	opens  = "({["
	closes = ")}]"
	return opens.index(o) == closes.index(c)

def checkParnthesis(sample):
	balanced = True
	index = 0
	s = myStack.Stack()
	while index < len(sample) and balanced :
		symbol = sample[index]

		if symbol in "({[" :
			s.push(symbol)
		else:
			
			if s.isEmpty() :
				balanced = False
			else:
				top = s.pop()
				if not matches(top,symbol):
					balanced = False

		index = index + 1

	if balanced and s.isEmpty():
		return balanced
	else:
		return False

print(checkParnthesis(""))






