# Given two strings of lowercase alphabets and a value k, the task is to find if two strings are K-anagrams of each other or not.
# Two strings are called k-anagrams if following two conditions are true. 

# Both have same number of characters.
# Two strings can become anagram by changing at most k characters in a string.


# Input:  str1 = "anagram" , str2 = "grammar" , k = 3
# Output:  Yes
# Explanation: We can update maximum 3 values and 
# it can be done in changing only 'r' to 'n' 
# and 'm' to 'a' in str2.
# Input:  str1 = "geeks", str2 = "eggkf", k = 1
# Output:  No
# Explanation: We can update or modify only 1 
# value but there is a need of modifying 2 characters. 
# i.e. g and f in str 2.

from collections import defaultdict

def are_k_anagaram(s1,s2,K):

    if len(s1) != len(s2):
        return False

    count = defaultdict(int)

    for ch in s1:
        count[ch] += 1
    
    for ch in s2:
        if count[ch] > 0:
            count[ch] -= 1
    
    diff_count = sum(count.values())

    if diff_count > K:
        return False
    else:
        return True

# Drive Code

if __name__=='__main__':
    str1 = "anagram"
    str2 = "grammar"
    k = 2
    
    if are_k_anagaram(str1, str2, k):
        print("Yes")
    else:
        print("No")
    