# This Code use for the Convert String in digit Followed Symbols

#input = 'a4b3c2'
#output = 'aaaabbbcc'

string = input("Enter a String Alphabets symbols followed by Digits output : ")
output = ' '

for ch in string:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output+(x*d)

print("Output String : ",output) 