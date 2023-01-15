def fact2(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

# here I'm using fact method beacuse if I'm using fact2 method then program complexcity will increase as per 
# current one.
def fact(n):
    res = 1
    for i in range(2,n+1):
        res = res*i
    return res

def combination(n,r):
    return (fact(n) / (fact(r) * fact(n-r)))
    
n=5
r=3
print("Combination is ", int(combination(n,r)))