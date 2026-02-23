#Using the input from the user, Generate the first N numbers of the Fibonacci sequence.
n = int(input("Enter how many Fibonacci numbers you want: "))

a = 0
b = 1

print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c