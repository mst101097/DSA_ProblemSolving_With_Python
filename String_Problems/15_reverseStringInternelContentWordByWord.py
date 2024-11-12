# reverse internel content word by word
# example :
# input = "this file is mohit "
# output = "siht elif si tihom "

string = input("enter the String : ")
l = string.split()
l1 = []
for Word in l:
    l1.append(Word[::-1])
# print(l1)
output = ' '.join(l1)
print(output)
