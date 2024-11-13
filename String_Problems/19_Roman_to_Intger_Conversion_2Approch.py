# Input: IX
# Output: 9
# Explanation: IX is a Roman symbol which represents 10 – 1 = 9


# Input: XL
# Output: 40
# Explanation: XL is a Roman symbol which represents 50 – 10 = 40


# Input: MCMIV
# Output: 1904
# Explanation: M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904

def romanToDecimal(s: str) -> int:
    roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    
    # Initialize result
    res = 0
    i = 0
    while i < len(s):
        # If the current value is less than the next
        # value, subtract current from next and add to sum
        if i+1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
           res = res + roman_map[s[i + 1]] - roman_map[s[i]]
           # Skip the next symbol
           i += 2
        else:

           # Otherwise, add the current value to sum
            res += roman_map[s[i]]
            i += 1
    return res

# Driver code
if __name__ == "__main__":
    s = "XI"
    print(romanToDecimal(s))