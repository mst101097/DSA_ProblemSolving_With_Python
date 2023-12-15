'''
Ternary operators are more commonly known as conditional expressions in Python.
These operators evaluate something based on a condition being true or not.
They
became a part of Python in version 2.4
'''

'''
Blueprint:
value_if_true if condition else value_if_false

'''
is_nice = True
state = "nice" if is_nice else "not nice"

'''
This is not recommended method as far:

It allows to quickly test a condition instead of a multiline if statement. Often times it
can be immensely helpful and can make your code compact but still maintainable.
Another more obscure and not widely used example involves tuples.

Blueprint:
(if_test_is_false, if_test_is_true)[test]
'''
nice = True
personality = ("mean", "nice")[nice]
print("The cat is ", personality)
# Output: The cat is nice