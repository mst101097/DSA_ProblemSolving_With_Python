
'''
set is a really useful data structure. sets behave mostly like lists with the distinction
that they can not contain duplicate values. It is really useful in a lot of cases. For
instance you might want to check whether there are duplicates in a list or not. You
have two options. The first one involves using a for loop. Something like this:

'''
# First method for remove duplicate in list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates =[]
for value in some_list:
    if some_list.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)

# print(f'Duplicates: ,{duplicates}')
#output-- Duplicates: ,['b', 'n']


# Second method through set
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates1 = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates1)
# Output: set(['b', 'n'])

# duplicates1 = list(set(some_list))

# Set have bulit in method 1. intersect 2. Difference
# 1. Intersect

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(f' intersect - {input_set.intersection(valid)}')

# 2. Difference 
print(f' Difference - {input_set.difference(valid)}')
# output  intersect - {'red'} , Difference - {'brown'}

