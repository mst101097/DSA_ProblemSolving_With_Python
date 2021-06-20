def binarySearch(a,x,si,ei,):
	if si>ei:
		return -1

	mid = (si+ei)//2

	if a[mid]==x:
		return mid
	if a[mid]>x:
		return binarySearch(a,x,si,mid-1)
	else:
		return binarySearch(a,x,mid+1,ei)

# First Array should be sorted

a = [1,3,4,5,7,8,9,12,12,23,56]
si = 0
ei = len(a)-1
x = 4
print(binarySearch(a,x,si,ei,))