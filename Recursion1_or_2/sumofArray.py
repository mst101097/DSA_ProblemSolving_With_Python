def SumofArray(arr,si):
	l = len(arr)
	if l==0:
		return 0
	else:
		return sum + SumofArray(arr,si+1)

a = [1,2,3,4,5,5]
si = 0
print(SumofArray(a,si))



