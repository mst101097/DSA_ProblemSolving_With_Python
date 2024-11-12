# This Code using for the find the Vowel Occurrance in Given String 
# inputsting = 'durgasoftwareaeiou'

S = input('Enter the Given string to find vowel Occerrance : ')
vowelList = ['A','E','I','O','U','a','e','i','o','u']
charDict = {}

for char in S:
    if char in vowelList:
        charDict[char] = charDict.get(char,0)+1

# print(charDict) #{'u': 1, 'a': 2, 'o': 1, 'e': 1}

for k,v in sorted(charDict.items()):
    print(f'{k} Occerrance {v} times ')

#output:
# a Occerrance 3 times 
# e Occerrance 2 times
# i Occerrance 1 times
# o Occerrance 2 times
# u Occerrance 2 times

# if interviewr asking about string output looklike : 'a2e1o1u1' than using this code

# output = ''
# for k,v in sorted(charDict.items()):
#     output = output+k+str(v)

# output :  a3e2i1o2u2


print('output : ',output)







