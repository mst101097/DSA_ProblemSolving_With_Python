# Union and Intersection of two sorted arrays
# Input : arr1[] = {1, 3, 4, 5, 7}
#         arr2[] = {2, 3, 5, 6}
# Output : Union : {1, 2, 3, 4, 5, 6, 7}
#          Intersection : {3, 5}

def unionOfArray(arr1,arr2,m,n):
	i,j = 0,0

	while i<m and j<n:
		if arr1[i]<arr2[j]:
			print(arr1[i],end=' ')
			i =i+1

		elif arr2[j]<arr1[i]:
			print(arr2[j],end=' ')
			j = j+1

		else:
			print(arr2[j],end=' ')
			j = j+1
			i= i+1

	while i<m:
		print(arr1[i],end=' ')
		i =i+1

	while j < n:
		print(arr2[j],end=' ')
		j =j+1

def interSectionOfArray(arr1,arr2,m,n):

	i,j =0,0

	while i<m and j<n:
		if arr1[i]<arr2[j]:
			i =i+1
		elif arr2[j]<arr1[i]:
			j = j+1
		else:
			print(arr2[j],end =' ')
			j =j+1
			i = i+1


arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
print('--------------Union Of Array ------------')

unionOfArray(arr1,arr2,m,n)
print()
print('-------------InterSection Of Array---------')
interSectionOfArray(arr1,arr2,m,n)
print()


