import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return round(math.sqrt(self.x**2 + self.y**2))

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  # Output: Vector(4, 6)
print(v1 - v2)  # Output: Vector(-2, -2)
print(v1 * 2)   # Output: Vector(2, 4)
print(v1 == v2) # Output: False
print(len(v1))  # Output: 2
print(v1[0])    # Output: 1
print(v1[1])    # Output: 2

'''
Vector Class is a class that represents a vector in 2D space. 
It provides methods for vector addition, subtraction, multiplication, 
equality comparison, length calculation, and element access.

The class has the following features:

- __init__(): Initializes the vector with x and y coordinates.
- __repr__(): Returns a string representation of the vector.
- __add__(): Adds two vectors component-wise.
- __sub__(): Subtracts two vectors component-wise.
- __mul__(): Multiplies a vector by a scalar.
- __eq__(): Checks if two vectors are equal.
- __len__(): Returns the length of the vector.
- __getitem__(): Allows access to vector components by index.

This class provides a simple and intuitive way to work with vectors in 2D space.
'''
