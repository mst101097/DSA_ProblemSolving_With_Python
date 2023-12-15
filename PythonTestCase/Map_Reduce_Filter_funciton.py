'''
Map function -- Map applies a function to all the items in an input_list. Here is the blueprint:

map(function_to_apply, list_of_inputs)
'''

def multiply(x):
    return x*x

def add(x):
    return x+x

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    # print(value)

'''
ouput :
[0, 0]
[1, 2]
[4, 4]
[9, 6]
[16, 8]
'''
# Fliter - Filter create list of elements for which function return true

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
# print(f'less_than_zero :{less_than_zero}')
# output = less_than_zero :[-5, -4, -3, -2, -1]

'''
Reduce is a really useful function for performing some computation on a list and returning
the result. It applies a rolling computation to sequential pairs of values in a
list. For example, if you wanted to compute the product of a list of integers
'''

#basic login for result
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
# print(product)

# through Reduce function 
from functools import reduce
product = reduce((lambda x,y : x * y),[1,2,3,4])
print(product)
