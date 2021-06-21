def findMaxMin(low,high,arr):
    arrMin = arr[low]
    arrMax = arr[low]

    # if there is only one element in Array
    if low == high:
        arrMax = arr[low]
        arrMin = arr[low]
        return(arrMax, arrMin)
    
    # if there is only to 2 element  in array which is need compaision both element
    elif high==low+1:
        if arr[low]>arr[high]:
            arrMax = arr[low]
            arrMin = arr[high]
        else:
            arrMax =arr[high]
            arrMin = arr[low]
        return (arrMax, arrMin)

    else:
        mid = int((low+high)//2)
        arrMax1,arrMin1 = findMaxMin(low,mid,arr)
        arrMax2,arrMin2 = findMaxMin(mid+1,high,arr)

        return (max(arrMax1,arrMax2),min(arrMin1,arrMin2))
    
arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = findMaxMin(low, high, arr)
print('arrMax : ' ,arr_max)
print('arrMin : ' ,arr_min)
        
    
        

    