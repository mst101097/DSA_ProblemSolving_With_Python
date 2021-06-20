def fibnonic(n):
	if n==1 or n==2:
		return 1
	fib_of_1 = fibnonic(n-1)
	fin_of_2 = fibnonic(n-2)
	output = fib_of_1 + fin_of_2
	return output

n = 4
for i in range(1, n):
	print(fibnonic(i))