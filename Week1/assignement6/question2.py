#Extract all integers from a list that are greater than 10. Using List Comprehensions
#numbers = [1, 5, 13, 4, 16, 7]
#Expected output :[13, 16]

numbers=[1,5,13,4,16,7]

new_list=[num for num in numbers if num>10]

print(new_list)