def powerofElement_firstMethod(x,n):
	if n==0:
		return 1
	else:
		return x * powerofElement_firstMethod(x,n-1)


def powerOfElement_secondMethod(x,pow):
	if pow == 0:
		return 1
	smallpower  = powerOfElement_secondMethod(x,pow//2)

	if pow%2==0:
		return smallpower * smallpower
	else:
		return x * smallpower * smallpower
		


print(powerOfElement_secondMethod(2,3))


