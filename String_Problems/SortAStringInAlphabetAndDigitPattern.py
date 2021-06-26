# This code use for Sort a String in Alphabets and digit format
# input = 'B4A1D3'
#output = 'ABD134'

str1 = 'B4A1D3'
alphabets = []
digit = []

for ch in str1:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digit.append(ch)

output = ''.join(sorted(alphabets)+sorted(digit))

print('SortString : ',output)

