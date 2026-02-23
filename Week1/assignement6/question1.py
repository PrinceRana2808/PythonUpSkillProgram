"""Given a list of numeric strings, convert them into integers. Using List Comprehensions
strings = ["1", "2", "3", "4", "5"]
Expected output : [1, 2, 3, 4, 5]
"""

strings = ["1", "2", "3", "4", "5"]
print(strings)

numbers = [i for i in range(len(strings))]
print(numbers)