# This code using string character occurance With NumberCount(StringCompress_Problem)

#inputString = "aaaabbbcccczz"
#outputString = "a4b3c4z2"

# 1st Method

inputStr = input("Enter String : ")
n = len(inputStr)
previousChar = inputStr[0]
output = ' '
counter = 1
i  = 1

while i<n:
    if inputStr[i]==previousChar:
        counter = counter+1
    
    else:
        output = output+previousChar+str(counter)
        previousChar = inputStr[i]
        counter = 1
    
    # this Code line using for last character counter add
    if i == n-1:
        output = output+previousChar+str(counter)

    i = i+1
    
print("outputString : ", output)

Enter String : aaaabbbcccczz
outputString :   a4b3c4z2


# 2nd Method (Using Dict() dataStructure)

S = 'aaaabbbcccczz'
charDict = {}

for ch in S:
    charDict[ch] = charDict.get(ch,0)+1

# print(charDict) # {'a': 4, 'b': 3, 'c': 4, 'z': 2}

output = ""

for k,v in charDict.items():
    output = output+str(v)+k

print("output : ", output)
#output :  4a3b4c2z

# if you want the this type a4b3c4z2  then changes the some code accoordingly

# for k,v in charDict.items():
#     output = output+k+str(v)

# print("output : ", output)
#output will be a4b3c4z2








