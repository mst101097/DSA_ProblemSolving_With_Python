# Sort an array of 0s, 1s and 2s
# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

# inputArr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

# outputArr = [0, 0 ,0 ,0, 0, 1, 1, 1 , 1, 1, 2, 2]

def SortZeroOneTwo_oneSide(arr):
	n = len(arr)

	c0 = 0
	c1 = 0
	c2 = 0

	# counter Part
	for i in range(n):
		if arr[i] == 0:
			c0 = c0+1

		if arr[i]== 1:
			c1 = c1+1

		if arr[i]== 2:
			c2 = c2+1

	# Updation Part
	i = 0

	while c0 > 0:
		arr[i] = 0
		i = i+1
		c0 =c0-1

	while c1 >0:
		arr[i] = 1
		i = i+1
		c1 =c1-1

	while c2>0:
		arr[i] = 2
		i =i+1
		c2 =c2-1

arr= [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
SortZeroOneTwo_oneSide(arr)
print(arr)