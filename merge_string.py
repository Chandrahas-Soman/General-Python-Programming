# merge string in a specific way

def mergeStrings(a,b):
	m = list(a)
	n = list(b)
	ret = []

	if len(m) < len(n):
		for i in range(0, len(m)): 
			ret.append(m[i])
			ret.append(n[i])
		ret.append(b[len(m):])

	else:
		for i in range(0, len(n)): 
			ret.append(m[i])
			ret.append(n[i])
		ret.append(a[len(n):])
	
	print('').join(ret)

mergeStrings('abc', 'stuvwxyz')