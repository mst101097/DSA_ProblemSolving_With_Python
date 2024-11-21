# Input: str = “(())))(“
# Output:   4
# Explanation: After index 4, string splits into (()) and ))(. The number of opening brackets in the first part is equal to the number of closing brackets in the second part.


# Input: str = “))”
# Output: 2
# Explanation: As after 2nd position i.e. )) and “empty” string will be split into these two parts. So, in this number of opening brackets i.e. 0 in the first part is equal to the number of closing brackets in the second part i.e. also 0.


def findIndex(S):
    count_close = 0
    L = len(S)

    for i in range(0,L):
        if S[i] == ')':
            count_close  = count_close + 1
    
    for i in range (0, L):
        if count_close == i:
            return i 
    return L

# Driver Code 
str = "(()))(()()()))"
print(findIndex(str)) 