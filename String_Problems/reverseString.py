# Reverse String Mutiple types

# First method  reverse by Negative index
inputSting  = input("enter String :")
outputString = inputSting[::-1]
print('Reverse String :',outputString)


# Second Method Through Reversed inbulid Functions
s = input("Enter String : ")
r = reversed(s)
output = ''.join(r)
print(output)


# Third Method Through While Loop
inputStr = input("Enter String : ")
output = ''
i = len(inputStr)-1
while i>=0:
    output = output+inputStr[i]
    i = i-1
print(output)
