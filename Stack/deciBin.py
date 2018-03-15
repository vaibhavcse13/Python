import myStack 

def divideBy2(num , base):
	digits = "0123456789ABCDEF"
	s = myStack.Stack()

	while num > 0 :
		rem = num % base
		s.push(rem)
		num = num // base
		

	binaryStr = ""

	while  not s.isEmpty():
		binaryStr = binaryStr  +  digits[s.pop()]

	return binaryStr


print(divideBy2(26 , 26))