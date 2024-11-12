# THis code use for crete a string in alphabets followed digits in Sorted

#inputString = 'a4z2b3y3'
#outputString = 'aaaabbbyyyzz'

str1 = input("Enter the String which alphabets followed digits : ")
target = ""

for ch in str1:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        target = target+(x*d)

# print(target)
# if I printed the target here output will be 'aaaazzbbbyyy' but we will looking for sorted form of string so I used sorted method 

output = ''.join(sorted(target))
print("OutputString : ",output)

# Enter the String which alphabets followed digits : a4z2b3y3
# OutputString :  aaaabbbyyyzz

