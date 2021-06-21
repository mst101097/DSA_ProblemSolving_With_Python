def RotationIndex(arr,d):
    for i in range(d):
        rotationByOne(arr)

def rotationByOne(arr):
    length = len(arr)

    tempVar = arr[0]
    for i in range(length-1):
        arr[i] = arr[i+1]
    arr[length-1] = tempVar

# a = [1, 3, 2, 3, 4, 5, 5, 6]
a = [1, 3, 2, 3, 4, 5, 5, 6]
print("Before",a)
RotationIndex(a,2)
print("after",a)

