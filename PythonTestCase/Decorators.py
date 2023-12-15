'''
Decorators are a significant part of Python. In simple words: they are functions which
modify the functionality of other functions. They help to make our code shorter and
more Pythonic. Most beginners do not know where to use them so I am going to share
some areas where decorators can make your code more concise.

2. They take function as a Arugment and modify the function functionality.



a decorator is a special type of function that is used to modify the behavior of another function. Decorators are a powerful and flexible way to extend or modify the functionality of functions without changing their actual code. They are often used for tasks such as logging, timing, caching, access control, 

'''
#Point 1 - Returning functions from within functions
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"
    def welcome():
        return "now you are in the welcome() function"
    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
# print(a)
#outputs: <function greet at 0x7f2143c01500>

# print(a())
#outputs: now you are in the greet() function


#Point 2 Giving a function as an argument to another function:
def hi():
    return "hi yasoob!"
def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())
# doSomethingBeforeHi(hi)
#outputs:I am doing some boring work before executing hi()
# hi yasoob!


# point 3 Writing your first decorator

def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

# a_function_requiring_decoration()

# ponit 4 other type to call decorator
@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


# a_function_requiring_decoration()

# Example 1

# Decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Function decorated with my_decorator
# @my_decorator
# def say_hello():
#     print("Hello!")

# # Calling the decorated function
# say_hello()


# Example 2
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
