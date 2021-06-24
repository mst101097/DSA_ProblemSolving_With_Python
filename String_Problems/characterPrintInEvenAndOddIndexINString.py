# Print Character in Even index and Odd Index

#FirstMethod
string  = input("Enter the String : ")
i=0
print("Even index Character :")
while i<len(string):
    print(string[i])
    i = i+2

print("Odd Index Character : ")
i = 1 
while i<len(string):
    print(string[i],end=" ")
    i = i+2

#second method
print("Even Index Character : ",string[0: :2])
print("Odd Index Character : ",string[1: :2])