#Use reduce() and lambda to find the longest word in a list of strings.
#from functools import reduce
#Expected Output: 'banana'

from functools import reduce
words = ["apple", "banana", "cherry", "date"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)

print(longest)