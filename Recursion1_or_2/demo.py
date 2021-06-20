# def lowercase_decorater(function):
# 	def warrap():
# 		fun = function()
# 		string_lower = fun.lower()
# 		return string_lower
# 	return warrap

# @lowercase_decorater
# def hello():
# 	return"HELLO MOHIT"

# print(hello())

def names_decorator(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1, arg2)
        return string_hello
    return wrapper

@names_decorator
def hello(args1,args2):
	return "first "+ args1 + " Lastname " + args2

print(hello('mohit','singh'))
