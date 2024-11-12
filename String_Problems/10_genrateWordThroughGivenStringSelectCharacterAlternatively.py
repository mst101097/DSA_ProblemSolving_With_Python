# This code usring for Genrated word through multiple String character alternatively

s1 = str(input('Enter your First String : '))
s2 = str(input('Enter your second String : '))
s3 = str(input('Enter your Thrid String : '))

i=j=k=0

while i<len(s1) or j<len(s2) or k<len(s3):
    output = " "
    if i<len(s1):
        output = output+s1[i]
        i = i+1

    if j<len(s2):
        output = output+s2[j]
        j = j+1

    if k<len(s3):
        output = output+s3[k]
        k = k+1

    print(output,end=",")

# Enter your First String : abcdefg
# Enter your second String : xyxz
# Enter your Thrid String : 12345
# Output :  ax1, by2, cx3, dz4, e5, f, g,

