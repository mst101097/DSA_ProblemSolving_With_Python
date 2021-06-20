def fact(n):
	if n == 0:
		return 1
	return n * fact(n-1)


def sum_N(n):
	if n==0:
		return 0
	smallOutput = sum_N(n-1)
	Output = smallOutput + n
	return Output

def printNaturalNumber(n):
	if n==0:
		return
	printNaturalNumber(n-1)
	print(n)
	return

# print reverse n natural number
def printNnumber(n):
	if n==0:
		return
	print(n)
	printNnumber(n-1)
	return



n = int(input('enter the numnber '))
print(fact(n))
print(sum_N(n))
print(printNaturalNumber(n))
print(printNnumber(n))
