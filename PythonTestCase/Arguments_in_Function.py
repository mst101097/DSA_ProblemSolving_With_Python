#Usage of *args(argument)

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)
#test_var_args('yasoob', 'python', 'eggs', 'test')


# Usage of **kwargs(Keyword Argument)

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
#greet_me(name='mohit',msg='Hello')

#Using *args and **kwargs to call a function
def test_arg_kward(arg1,arg2,arg3):
    print(f'arg1-',{arg1})
    print(f'arg3-',{arg2})
    print(f'arg3-',{arg3})

args = ("two", 3, 5)
# test_arg_kward(*args)

# now with **kwargs:
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_arg_kward(**kwargs)


