# Input: IX
# Output: 9
# Explanation: IX is a Roman symbol which represents 10 – 1 = 9


# Input: XL
# Output: 40
# Explanation: XL is a Roman symbol which represents 50 – 10 = 40


# Input: MCMIV
# Output: 1904
# Explanation: M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904


# This function returns value of a Roman symbol
def value(r: str) -> int:
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1


def Roman_To_Decimal(s):
    # intialze res =0
    res = 0
    
    i=0
    while i <len(s):
        # Get value of current symbol
        s1  = value(s[i])

        # Compare with the next symbol if it exists
        if i+1 < len(s):
            s2  = value(s[i+1])

            # If current value is greater or equal,
            # add it to result

            if s1 >= s2:
                res = res+s1
            else:
                # Else, add the difference and skip
                # next symbol
                res = res + (s2-s1)
                i = i+1
        else:
            res += s1
        i += 1
    return res


# Driver code
if __name__ == "__main__":
    s = "X"
    print(Roman_To_Decimal(s)) 




