# Given a string Str. The task is to check if it is Pangram or not. 

# A pangram is a sentence containing every letter in the English Alphabet.


# Input: “The quick brown fox jumps over the lazy dog” 
# Output: is a Pangram 
# Explanation: Contains all the characters from ‘a’ to ‘z’] 


# Input: “The quick brown fox jumps over the dog”
# Output: is not a Pangram 
# Explanation: Doesn’t contain all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing

# Second Approch through set()
def checkPanagram(S):
    #first need and set datastructure container
    char_set =  set()

    for ch in S:
        if ch >= 'a' and ch <= 'z':
            char_set.add(ch)
        
        if ch >= 'A' and ch <= 'Z':
            ch  =  ch.lower()
            char_set.add(ch)
        
    if len(char_set) == 26:
        return True
    return False

# sentence = "The quick brown fox jumps over the little lazy dog"
sentence = "The quick brown fox jumps over the dog"
 
if (checkPanagram(sentence)):
    print('"'+sentence+'"')
    print("\nis a pangram")
else:
    print('"'+sentence+'"')
    print("\nis not a pangram")