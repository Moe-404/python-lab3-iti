from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p) # Output: Point(x=1, y=2)

# In this example:
# - The Point class automatically receives an __init__ method, 
# allowing for easy instantiation.

# - The __repr__ method is also automatically added, 
# making it easier to print the object.

'''
Data Class is a decorator (@dataclass) introduced in Python 3.7 to simplify the creation
of classes that primarily store data. By using this decorator, Python automatically adds
special methods to the class, such as __init__(), __repr__(), and __eq__(), reducing
boilerplate code. This feature is particularly useful for classes that are essentially
data containers.
'''