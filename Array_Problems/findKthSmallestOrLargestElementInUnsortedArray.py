# This code using for find smallest and largest element in particular unsorted array
# arr = [12, 3, 5, 7, 19]
# kth element = 2 #5 


def kthElementInArray(arr,k,n):
    # where arr = list of element, k = index of kth element , n =len of list(array)
    arr.sort()

    return arr[k-1]

arr = [12, 3, 5, 7, 19]
n = len(arr)
k = 2
print('kth smallest Element : ',kthElementInArray(arr,k,n))

