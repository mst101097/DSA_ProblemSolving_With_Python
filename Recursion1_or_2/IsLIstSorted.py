def isListsorted(arr):
	l = len(arr)

	if l==0 or l==1:
		return True
	if arr[0]>arr[1]:
		return False

	smallerList = arr[1:]

	issmallerListSorted = isListsorted(smallerList)

	if issmallerListSorted:
		return True
	else:
		return False

# Second method

def isListSortedInBetterWay(arr,si):
	l = len(arr)

	if si == l-1 or si ==l:
		return True

	if arr[si]>arr[si+1]:
		return False

	isSmallerSorted = isListSortedInBetterWay(arr,si+1)

	return isSmallerSorted




a = [1,2,3,4,5,6,7,8,9,10]
print(isListSortedInBetterWay(a,si=0))
