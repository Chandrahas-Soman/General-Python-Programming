#Given a number, count number of 1s in its binary form.

def countSetBits(n):
	a = bin(n)
	b = []
	ret = []
	print(a)
	counter = -2
	b = a.split('1')
	print(b)
	ret.append(len(b) -1)
	for i in a:
		counter = counter + 1 
		print (counter)
		if i == '1':
			ret.append(counter)
	
	print(len(b) - 1)
	print (ret)

countSetBits(4)
