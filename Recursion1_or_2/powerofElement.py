def powerofElement(x,n):
	if n==0:
		return 1
	else:
		return x * powerofElement(x,n-1)


print(powerofElement(2,3))


