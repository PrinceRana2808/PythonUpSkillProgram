#Given a list let's see how to double each element of the given list. Using map() 
#Expected Output: [2, 4, 6, 8]

a = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, a))

print(result)