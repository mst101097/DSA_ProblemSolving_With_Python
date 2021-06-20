def firstIndex(arr,x):
	l = len(arr)

	if l==0:
		return -1
	if arr[0]== x:
		return 0

	smallerList = arr[1:]
	smallerListOutput = firstIndex(smallerList,x)

	if smallerListOutput == -1:
		return -1
	else:
		return smallerListOutput+1

#Second Method With Starting index


def firstIndexB(arr,x,si):
	l = len(arr)

	if si == l :
		return -1

	if arr[si] == x:
		return si

	smallerListOutput = firstIndexB(arr,x,si+1)
	return smallerListOutput

arr = [1,2,3,4,5,6,7,3]
x = 6
print(firstIndexB(arr,x,0))
