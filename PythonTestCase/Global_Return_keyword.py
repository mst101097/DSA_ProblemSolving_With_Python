# def add(value1, value2):
#     result = value1+value2

# print(result)
'''
Track back error.
NameError: name 'result' is not defined

'''

# if declare result as Global then result will be change

def add(value1, value2):
    global result
    result = value1+value2
add(2,4)
print(result)
#6

#3.8.1 Multiple return values
