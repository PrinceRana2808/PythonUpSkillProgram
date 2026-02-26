#Use filter() and lambda to extract all even numbers from a list of integers.
#Expected Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result=list(filter(lambda x:x%2==0,numbers))
print(result)