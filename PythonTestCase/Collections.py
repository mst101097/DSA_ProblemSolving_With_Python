'''
Python ships with a module that contains a number of container data types called
Collections. We will talk about a few of them and discuss their usefulness.
The ones which we will talk about are:
• defaultdict
• OrderedDict
• Counter
• deque
• namedtuple
• enum.Enum (outside of the module; Python 3.4+)
'''
# defaultdict
from collections import defaultdict

colours = (
('Yasoob', 'Yellow'),
('Ali', 'Blue'),
('Arham', 'Green'),
('Ali', 'Black'),
('Yasoob', 'Red'),
('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)
# print(favourite_colours)
for name, colour in colours:
    favourite_colours[name].append(colour)
# print('favourite_colours contains-> ',favourite_colours)
'''
 defaultdict(<class 'list'>, {'Yasoob': ['Yellow', 'Red'], 'Ali': ['Blue', 'Black'], 'Arham': ['Green'], 'Ahmed': ['Silver']})

'''
'''
One other very important use case is when you are appending to nested lists inside a
dictionary. If a key is not already present in the dictionary then you are greeted with
a KeyError. defaultdict allows us to circumvent this issue in a clever way. First let
me share an example using dict which raises KeyError and then I will share a solution
using defaultdict.

Problem:

some_dict = {}
some_dict['colours']['favourite'] = "yellow"
# Raises KeyError: 'colours'
'''
from collections import defaultdict
tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
# Works fine

#Second way throgh json
import json
# print(json.dumps(some_dict))
# Output: {"colours": {"favourite": "yellow"}}


'''
# OrderedDict-
-----------------
OrderedDict keeps its entries sorted as they are initially inserted. Overwriting a value
of an existing key doesn't change the position of that key. However, deleting and
reinserting an entry moves the key to the end of the dictionary
'''

'''
Problem:
colours = {"Red" : 198, "Green" : 170, "Blue" : 160}
for key, value in colours.items():
    print(key,value)

output : 
Red 198
Green 170
Blue 160

here entry are present in unpredictable order, But Now using by collection OrderedDict
'''

from collections import OrderedDict
colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
# for key, value in colours.items():
#     print(key, value)
# Insertion order is preserved

'''
Counter
--------
Counter allows us to count the occurrences of a particular item. For instance it can be
used to count the number of individual favourite colours:

'''

from collections import Counter
colours = (
('Yasoob', 'Yellow'),
('Ali', 'Blue'),
('Arham', 'Green'),
('Ali', 'Black'),
('Yasoob', 'Red'),
('Ahmed', 'Silver'),
)
favs = Counter(name for name, colour in colours)
# print(favs)
'''
Output: Counter({
'Yasoob': 2,
'Ali': 2,
'Arham': 1,
'''
'''
We can also count the most common lines in a file using it. For example:
with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)
'''


'''
deque
======
deque provides you with a double ended queue which means that you can append
and delete elements from either side of the queue. First of all you have to import the
deque module from the collections library

'''
# Type1 for using deque
from collections import deque
d = deque()
d.append('1')
d.append('2')
d.append('3')
# print(len(d))
# print(d[0])

# Type 2 for using deque, you can pop values from both sides of the deque:
d = deque(range(5))
print(len(d))
# Output: 5
print(d.popleft())
# Output: 0
print(d.pop())
# Output: 4
print(d)
# Output:

