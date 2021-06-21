# a = [1, 3, 2, 3, 4, 5, 5, 6]

def pairOfSum(arr,targetSum):
    length = len(arr)
    # print(arr)
    i=0

    while(i<length):
        j = i+1
        if arr[i]+arr[j]==targetSum:
            print(i,j)
            i = i+1
            j = j+1
        else:
            j = j+1
            

a = [1, 3, 2, 3, 4, 5, 5, 6]
pairOfSum(a,7)
