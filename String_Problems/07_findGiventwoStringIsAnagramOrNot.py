# This Code use for find the string is anagram or Not
# Anagram Mean's A string has all character in compair String 
# like SILENT == LISTEN , lazy == zaly etc

str1 = input('Enter First stirng : ')
str2 = input('Enter Second string : ')

if sorted(str1)== sorted(str2):
    print('String is Anagram ')
else:
    print('String Not Anagram ')