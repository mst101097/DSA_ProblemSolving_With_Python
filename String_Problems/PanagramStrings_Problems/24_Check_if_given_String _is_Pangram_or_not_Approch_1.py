# Given a string Str. The task is to check if it is Pangram or not. 

# A pangram is a sentence containing every letter in the English Alphabet.


# Input: “The quick brown fox jumps over the lazy dog” 
# Output: is a Pangram 
# Explanation: Contains all the characters from ‘a’ to ‘z’] 


# Input: “The quick brown fox jumps over the dog”
# Output: is not a Pangram 
# Explanation: Doesn’t contain all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing


def checkStringPanagram(S):

    contain_array = []
    # create list of 26 characters and set false each entry
    for i in range(26):
        contain_array.append(False)
    

    for ch in S.lower():
        if not ch == " ":
            contain_array[ord(ch) - ord('a')] = True
            #print(ord('a'), ord(ch))

    #print(contain_array)
    for ch in contain_array:
        if ch == False:
            return False
    return True
    
# Driver Program to test above functions
sentence = "The quick brown fox jumps over the little lazy dog"
#sentence = "The quick brown fox jumps over the dog"
 
if (checkStringPanagram(sentence)):
    print('"'+sentence+'"')
    print("\nis a pangram")
else:
    print('"'+sentence+'"')
    print("\nis not a pangram")