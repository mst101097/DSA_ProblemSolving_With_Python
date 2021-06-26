# In this Problem I have 2 Possible way to remove duplicate character ib String

# (1) First way: This is recommanded way
# 'aaaaaaabbbcnskkkkkddddwwwwwss'

string = input("Enter your String : ")
output = ' '
for ch in string:
    if ch not in output:
        output = output + ch

print('outputString: ',output)

#  (2) Second Way :
#  'assdsddddssseeeetttww' 
S = input("Enter your String : ")
l = []

for ch in S:
    if ch not in l:
        l.append(ch)

outputString = ''.join(l)
print('outputString : ',outputString)


# 3rd Way: through Set() data Structure but in set order does not matter so if you look same order answer so use first two method they are easy ans Simple

# 'dssdasdsdkjskjkkkkjjjjjdhh'
inputString = input("Enter your String : ")
tempstring = set(inputString)
Output = ''.join(tempstring)
print("Output: ",Output)





