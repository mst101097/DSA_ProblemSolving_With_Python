# MergeTwo String in single string alternative charactor

# s1 = 'Ravi'
# s2 = 'Teja'
# output ='RTaevjia'

# first Mehtod is vaild for only Both string length is Same
s1 = 'Ravi'
s2 = 'Teja'
output =''
i,j = 0,0

while i<len(s1) or j<len(s2):
    output = output+s1[i]+s2[j]
    i = i+1
    j = j+1

print("MergeString : ",output)

# Second method is versatile for both condition if length of string less than each other but given vaild output 

s1 = input('Enter First String : ')
s2 = input('Enter Second String : ')
output =''
i,j = 0,0

while i<len(s1) or j< len(s2):
    if i<len(s1):
        output = output+s1[i]
        i = i+1
    
    if j < len(s2):
        output = output+s2[j]
        j = j+1

print("MergeString Output : ",output)
