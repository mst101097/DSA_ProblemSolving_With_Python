# In this method we move the target element in Oneside

# inputArr = [5,6,10,0,60,61,0,90,0]

# outputArr = [0,0,0,5,6,10,60,61,90]

def moveElmentOneSide(arr):
	readStream = len(arr)-1
	writeStream = len(arr)-1

	while readStream >= 0:
		if arr[readStream] != 0:
			arr[writeStream] = arr[readStream]
			writeStream = writeStream-1

		readStream = readStream-1

	while writeStream >=0:
		arr[writeStream] = 0
		writeStream = writeStream-1

arr1 = [5,6,10,0,60,61,0,90,0]
moveElmentOneSide(arr1)
print(arr1)


