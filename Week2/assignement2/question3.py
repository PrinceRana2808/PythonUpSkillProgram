#Determine if any number in a list is divisible by 5 an print.

numbers = [1, 3, 5, 7, 8]
result=any(num%5==0 for num in numbers)
print(result)
