'''
1. an iterator is an object that
enables a programmer to traverse a container, particularly lists. However, an iterator
performs traversal and gives access to data elements in a container, but does not perform
iteration.

-> Iterable -- An iterable is any object in Python which has an __iter__ or a __getitem__ method
defined which returns an iterator or can take indexes. In short an iterable is any object which can provide us with an iterator.

-> Iterator -- An iterator is any object in Python which has a next (Python2) or __next__ method
defined.That's an iterator.

-> Iteration -- In simple words it is the process of taking an item from something e.g a list. When
we use a loop to loop over something it is called iteration. It is the name given to the
process itself.

2. Generators are iterators, but you can only iterate over them once. Its because they do
not store all the values in memory, they generate the values on the fly. You use them
by iterating over them, either with a 'for' loop or by passing them to any function
or construct that iterates. Most of the time generators are implemented as functions.
However, they do not return a value, they yield it.

'''
def genrators_function():
    for i in range(10):
        yield(i)

# for item in genrators_function():
#     print(item)


# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

#Now we can use it like this:
# for x in fibon(1000000):
#     print(x)

#Second Type
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# genrator  functions
def generator_function2():
    for i in range(3):
        yield i

gen = generator_function2()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# # Output: 2
# print(next(gen))

my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
