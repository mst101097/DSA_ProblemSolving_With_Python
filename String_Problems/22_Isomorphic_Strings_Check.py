# Two strings s1 and s2 are called isomorphic if there is a one-to-one mapping possible for every character of s1 to every character of s2. And all occurrences of every character in ‘s1’ map to the same character in ‘s2’.

# Examples: 

# Input:  s1 = “aab”, s2 = “xxy”
# Output: True
# Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.


# Input:  s1 = “aab”, s2 = “xyz”
# Output: False
# Explanation: One occurrence of ‘a’ in s1 has ‘x’ in s2 and other occurrence of ‘a’ has ‘y’.


def is_isomorphic(s1,s2):
    if len(s1) != len(s2):
        return False
    
    m1 = dict()
    m2 = dict()

    for i in range(len(s1)):
        if s1[i] not in m1:
            m1[s1[i]] = i
        if s2[i] not in m2:
            m2[s2[i]] = i
    
        if m1[s1[i]] != m2[s2[i]]:
            return False
    print(m1,m2)
    return True

print("True" if is_isomorphic("aab", "xxy") else "False")