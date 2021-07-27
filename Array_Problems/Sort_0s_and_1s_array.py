# Segregate 0s and 1s in an array
# Sort an array 0s and 1s without sorting

# Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

def sort_0s_And_1s(arr):

	n = len(arr)

	count = 0

	# loop for 0 count
	for i in range(n):
		if arr[i]==0:
			count =count+1

	# loop for O intialize
	for i in range(0,count):
		arr[i] = 0

	# loop for 1 intialize in array
	for i in range(count,n):
		arr[i] = 1

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
sort_0s_And_1s(arr)
print(arr)