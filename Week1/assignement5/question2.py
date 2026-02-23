#Write a recursive function to compute the factorial of a non-negative integer.

def find_factorial(num):
    if num==1:
        return 1
    return num*find_factorial(num-1)

num=int(input("Enter a number whoose factorial to be find:"))

if num<=0:
    print("Enter positive integer")
else:
    fact=find_factorial(num)
    print(f"Factorial of {num} is {fact}")
