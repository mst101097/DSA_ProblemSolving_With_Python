'''
The mutable and immutable datatypes in Python cause a lot of headache for new
programmers.
mutable means 'able to be changed'. 
immutable means 'constant'.
'''

foo = ['hi']
print(foo)
# Output: ['hi']
bar = foo
bar += ['bye']
print(foo)
# Output: ['hi', 'bye']

# What just happened? We were not expecting that! We were expecting something 
foo = ['hi']
print(foo)
# Output: ['hi']
bar = foo
bar += ['bye']
print(foo)
# Expected Output: ['hi']
# Output: ['hi', 'bye']
print(bar)
# Output: ['hi', 'bye']

'''
It's not a bug. It's mutability in action. Whenever you assign a variable to another
variable of mutable datatype, any changes to the data are reflected by both variables.
The new variable is just an alias for the old variable. This is only true for mutable
datatypes.
'''

def add_to(num, target=[]):
    target.append(num)
    return target

temp1 = add_to(1)
print(temp1)
#[1]
temp2 = add_to(2)
print(temp2)
#[1,2]


#this is the diffrent approch to create a list in function if you passed the list in argument that provide you above result due to mutablety.
def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

res =add_to(42)
print(res)
res2 = add_to(43)
print(res2)





