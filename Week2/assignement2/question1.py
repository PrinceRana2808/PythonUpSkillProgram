#Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive.
# Using all() Input : numbers = [1, 2, 3, 4, 5] 
# #Expected Output : True


numbers = [1, 2, 3, 4, 5]

result = all(num > 0 for num in numbers)

print(result)