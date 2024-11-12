# Problem -> Longest comman perfix  problem(using sorting)

# Input: arr[] = [“geeksforgeeks”, “geeks”, “geek”, “geezer”]
# Output: gee
# Explanation: “gee” is the longest common prefix in all the given strings.


# Input: arr[] = [“hello”, “world”]
# Output: -1
# Explanation: There’s no common prefix in the given strings.

def LCP(arr):
    # first need to check the arr has the element 
    if not arr:
        return -1
    
    # if array have the element then need to sort the element for last and first element compair
    arr.sort()

    #Now need to get the first element and last element in temp variable for compair
    first = arr[0]
    last = arr[-1]

    # getting minlength for verify
    min_length = min(len(first),len(last))

    i = 0
    # Find the common prefix between the first
    # and last strings

    while i < min_length and first[i]==last[i]:
        i = i+1
        #print(f"first-> {first[i]}, Last -> {last[i]}\n")

    # Check if there's no common prefix
    if i==0:
        return -1

    return first[:i]
    

arr= ["geeksforgeeks", "geeks", "geek", "geezer"]
result =  LCP(arr)
print(f"Result-> ", result)