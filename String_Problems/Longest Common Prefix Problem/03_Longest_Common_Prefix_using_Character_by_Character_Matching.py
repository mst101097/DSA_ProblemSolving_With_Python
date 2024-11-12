# Problem  -> Finding the Longest comman prefix matching character by character

# Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
# Output : "gee"

# Input  : {"apple", "ape", "april"}
# Output : "ap"


# this is the helper function to find the minium length of string in given array 
def LCP_findMinLength_Helper(arr,n):
    min = len(arr[0])

    for i in range(1,n):
        if (len(arr[i]) < min):
            min = len(arr[i])
    
    return min


# A Function that returns the longest common prefix
# from the array of strings

def CommanPrefix(arr,n):
    minlen =  LCP_findMinLength_Helper(arr,n)

    result = ""

    for i in range(minlen):

        # Current character (must be same
        # in all strings to be a part of
        # result)
        current = arr[0][i]

        for j in range(1,n):
            if arr[j][i] != current:
                return result
        result  = result + current
    
    return result

if __name__ == '__main__':
    arr = ["geeksforgeeks", "geeks",
                    "geek", "geezer"]
    n = len(arr)
  
    ans = CommanPrefix(arr, n)
  
    if (len(ans)):
        print("The longest common prefix is ->",ans)
    else:
        print("There is no common prefix")



