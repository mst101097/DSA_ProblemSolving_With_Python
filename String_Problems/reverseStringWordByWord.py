# Reverse a String Word by Word
#input = "This is mohit file "
#output = "file mohit is This "

# First method through spliting and sliceing

string = input("Enter a String : ")
l = string.split()
print(l)
l1 = l[::-1]
print(l1)
output = ' '.join(l1)
print(output)

# short Approch
# string = input("Enter a String : ")
# l = string.split()
# output = ' '.join(reversed(l))
# print(output)

