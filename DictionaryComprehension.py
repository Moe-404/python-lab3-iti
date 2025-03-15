# Dictionary Comprehensions provide a concise way to create dictionaries in Python. 
# They are similar to list comprehensions but produce dictionary objects.

# Basic Syntax:

# {key: value for item in iterable}

# Example:

input_list = [(1, 'a'), (2, 'b'), (3, 'c')]

dictionary = {key: value for key, value in input_list}
print(dictionary)  # Output: {1: 'a', 2: 'b', 3: 'c'}

# In this example:
# - The input is a list of tuples, where each tuple contains a key and a value.
# - The dictionary comprehension iterates over each tuple in the list.
# - For each tuple, the key is assigned to the corresponding value in the dictionary.
# - The result is a dictionary where the keys are the numbers and the values are the letters.
