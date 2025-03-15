class A:
    def process(self):
        print("Process in A")

class B(A):
    def process(self):
        print("Process in B")

class C(A):
    def process(self):
        print("Process in C")

class D(B, C):
    pass

d = D()
d.process()

# In this example, D inherits from both B and C. 
# When d.process() is called, Python follows the MRO and calls the process method from class B. 
# The MRO can be inspected using the __mro__ attribute or the mro() method:

print(D.mro())
# Output: [D, B, C, A, object]
# This output indicates the order in which classes are searched for methods

'''
Multiple Inheritance in Python allows a class to inherit attributes and methods
from more than one parent class. This provides flexibility but can lead to complexities,
such as the Diamond Problem, where a particular method could be inherited from multiple paths.

To resolve such ambiguities, Python uses the Method Resolution Order (MRO), 
which determines the order in which base classes are searched when executing a method. 
Python's MRO follows the C3 linearization algorithm, ensuring a consistent and predictable order. 
'''