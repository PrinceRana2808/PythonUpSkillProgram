#Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], 
# use enumerate() to create a list of tuples where each tuple contains the index and the corresponding fruit,
#  but only for even indices.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

result = [(index, fruit) 
          for index, fruit in enumerate(fruits) 
          if index % 2 == 0]

print(result)