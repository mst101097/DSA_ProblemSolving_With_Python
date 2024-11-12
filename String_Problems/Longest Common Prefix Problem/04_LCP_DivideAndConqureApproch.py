# Problem-> Finding Longest Common Prefix using Divide and Conquer Algorithm


# Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
# Output : "gee"

# Input  : {"apple", "ape", "april"}
# Output : "ap"

# A Utility Function to find the common 
# prefix between strings- str1 and str2 
def CommanPrefix_helper(s1,s2):
    result = ""
    n1, n2  =  len(s1),len(s2)
    i, j = 0, 0

    while i <= n1-1 and j <= n2-1:
        if s1[i] != s2[j]:
            break
        result =  result + s1[i]
        i = i+1
        j = j+1
    
    return result

# A Divide and Conquer based function to 
# find the longest common prefix. This is 
# similar to the merge sort technique 
def CommanPrefix(arr,low,high):
    if low == high:
        return arr[low]
    
    if high > low:
        mid = low + (high - low)//2

        str1 = CommanPrefix(arr,low,mid)
        str2 = CommanPrefix(arr,mid+1, high)

        return CommanPrefix_helper(str1, str2)
    
# Driver Code
if __name__ == "__main__":
 
    arr = ["geeksforgeeks", "geeks", 
                   "geek", "geezer"] 
    n = len(arr)
    ans = CommanPrefix(arr, 0, n - 1) 
 
    if len(ans): 
        print("The longest common prefix is", ans)
    else:
        print("There is no common prefix") 