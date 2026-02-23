"""Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
Expected output : {'a': 1, 'b': 2, 'c': 3}
"""

keys = ['a', 'b', 'c']
values = [1, 2, 3]

result = {k: v for k, v in zip(keys, values)}

print(result)