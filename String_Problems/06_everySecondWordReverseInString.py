# In this problem Solve Every second word Reverse in given String
#input = "one two three four five six"
#output = "one owt three ruof five xis"

string = input("Enter your string : ")
l = string.split()
l1 = []
i = 0

while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i = i+1
# print(l1)
output = ' '.join(l1)
print(output)