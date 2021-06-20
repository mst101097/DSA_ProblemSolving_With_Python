def merge(arr1,arr2,arr3):
	i = 0
	j = 0
	k = 0

	while i<len(arr1) and j<len(arr2):
		if arr1[i]<arr2[j]:
			arr3[k] = arr1[i]
			k = k+1
			i = i+1
		else:
			arr3[k] = arr2[j]
			k = k+1
			j = j+1
	while i<len(arr1):
		arr3[k] = arr1[i]
		k = k+1
		i = i+1

	while j<len(arr2):
		arr3[k] = arr2[j]
		k = k+1
		j = j+1



def MargeSort(arr):
	if len(arr)==0 or len(arr)==1:
		return

	mid = len(arr)//2
	a1 = arr[0:mid]
	a2 = arr[mid:]

	MargeSort(a1)
	MargeSort(a2)

	merge(a1,a2,arr)

a = [10,23,53,3,6,7,8,3,1,2,10]

MargeSort(a)

print(a)