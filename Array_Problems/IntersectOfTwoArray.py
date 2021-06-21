def intersectOfArray(array1,array2,n,m):
    # where n is length of array1
    # m is length of array2
    i = 0
    j = 0

    while(i<n and j<m):

        if array1[i]>array2[j]:
            j = j+1
        elif array2[j]>array1[i]:
            i = i+1
        else:
            print(array1[i],end=" ")
            i = i+1
            j = j+1


a = [1, 3, 2, 3, 4, 5, 5, 6]
b = [3, 3, 5]

n = len(a)
m = len(b)

intersectOfArray(a,b,n,m)
