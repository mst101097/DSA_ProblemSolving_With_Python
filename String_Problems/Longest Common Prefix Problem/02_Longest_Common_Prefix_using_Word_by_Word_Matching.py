# Problem -> Longest Common Prefix using Word by Word Matching

# Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
# Output : “gee”

# Input  : {“apple”, “ape”, “april”}
# Output : “ap”

# this is the helper function that take the 2 string and return the compair result
def CommanPrefix_helper(s1,s2):
    res = ""
    length = min(len(s1), len(s2))

    for i in range(length):
        if s1[i] != s2[i]:
            break
        res =  res+s1[i]
    
    return res

#this is the function that take the array of string collection 
def comman_prefix(arr):
    prefix = arr[0]

    for i in range(1, len(arr)):
        prefix = CommanPrefix_helper(prefix,arr[i])
    
    return prefix

if __name__ == '__main__':
    # arr= ["geeksforgeeks", "geeks", "geek", "geezer"]
    arr = ["apple", "ape", "april"]
    result =  comman_prefix(arr)
    print(f"Result-> ", result)