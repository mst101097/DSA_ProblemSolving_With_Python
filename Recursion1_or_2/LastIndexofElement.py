def lastIndex(a,x):
	# Where a is List of Array and x is search element
	l = len(a)
	if l==0:
		return -1
	smallerList = a[1:]
	smallerListOutput = lastIndex(smallerList,x)

	if smallerListOutput != -1:
		return smallerListOutput + 1
	else:
		if a[0]==x:
			return 0
		else:
			return -1

# second Method
def lastindexB(a,x,si):
	l = len(a)
	if si == l:
		return -1

	smallerListOutput = lastindexB(a,x,si+1)

	if smallerListOutput != -1:
		return smallerListOutput
	else:
		if a[si] == x:
			return si
		else:
			return -1


a = [1,4,5,4,8]
x =4
print(lastindexB(a,x,0))

