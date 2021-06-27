# This code use for find out the count of character occrrance in given String

# 1st Method Through Count() Function
# S = 'abbacabbc'

S = input('Enter Your string : ')
l = []

for ch in S:
    if ch not in l:
        l.append(ch)
    
for ch in sorted(l):
    print(f'{ch} Occurr {S.count(ch)} times')

# 2nd Method  Through Set() data Structure


String = 'ddffsssdddvvff'
s1 = set(String)
print('---------------------')
for ch in sorted(s1):
    print(f'{ch} Occurr {String.count(ch)} times')

# 2nd Method Usind Dict()

s = input("Enter the String : ")
Dict = {}

for ch in s:
    Dict[ch] = Dict.get(ch,0)+1

# this line of code using for Show the items pair same to same storage pattern
for k,v in Dict.items():
    print(f'{k} Occurr {v} times')

# if you want to find the sorted pattern then using this line of code

for k,v in sorted(Dict.items()):
    print(f'{k} occurrance: {v} times ')




