# This code using string character occurance With NumberCount(StringCompress_Problem)

#inputString = "aaaabbbcccczz"
#outputString = "a4b3c4z2"

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

# Enter String : aaaabbbcccczz
# outputString :   a4b3c4z2
