# This code use for find out the count of character occrrance in given String

# 1st Method Through list

S = 'abbacabbc'
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


