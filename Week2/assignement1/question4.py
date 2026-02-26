#Use map() to square each number in the list and round the result to one decimal place.
#Expected Output: [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

result=list(map(lambda x:round(x**2, 1),my_floats))
print(result)