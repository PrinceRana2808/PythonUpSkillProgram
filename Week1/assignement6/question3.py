#Create a list of squares for numbers from 1 to 5. Using List Comprehensions
#Expected output :[1, 4, 9, 16, 25]

numbers=[1,4,9,16,25]
result=[num*num for num in numbers]

print(result)