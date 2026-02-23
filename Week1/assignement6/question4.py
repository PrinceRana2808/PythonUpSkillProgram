#Convert a 2D list into a 1D list.Using List Comprehensions
#Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]

matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]

result=[num for row in matrix for num in row]
print(result)