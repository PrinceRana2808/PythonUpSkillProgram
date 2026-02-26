#Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
#Expected Output: 

numbers = [1, 3, 5, 7, 8]

result=any(num%2==0 for num in numbers)
print(result)