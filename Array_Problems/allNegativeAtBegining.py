# Move all negative numbers to beginning and positive to end with constant extra space
# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5


def allNegativeAtBegining(arr,left,right):

	while left<=right:
		# Condition to check if the left and right pointer negative
		if arr[left] < 0 and arr[right] < 0:
			left = left+1

		# Condition to check if the left pointer is positive and right pointer as well
		elif arr[left]>0 and arr[right]>0:
			right= right-1

	# Condition to check if the left pointer element is positive and the right pointer element is negative
		elif arr[left]>0 and arr[right]<0:

			arr[left],arr[right] = arr[right],arr[left]
			left = left+1
			right = right-1

		else:
			left = left+1
			right = right-1

def printAllElement(arr):
	for i in arr:
		print(i, end=" ")
	print()

arr = [-12, 11, -13, -5, 6, -7, 5, -3, 11]
left = 0
right = len(arr)
allNegativeAtBegining(arr,left,right-1)
printAllElement(arr)
