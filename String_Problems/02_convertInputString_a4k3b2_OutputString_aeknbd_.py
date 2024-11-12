# In this code first find the char unicode value than check next unicode character to add in string previous char

# 1. ord() : To find unicode value to given character
#example : Print(ord('a')) #97

# 2. chr() : To find the character with Given unicode value 
#example : Print(chr(98)) #b

# inputString = 'a4k3b2'
# outputString = 'aeknbd'

S = input("Enter your String : ")
output = ''

for ch in S:
    if ch.isalpha():
        output = output+ch
        x = ch
    else:
        d = int(ch)
        newChar = chr(ord(x)+d)
        output = output+newChar

print("outputString : ", output)

# Enter your String : a4k3b2
# outputString :  aeknbd