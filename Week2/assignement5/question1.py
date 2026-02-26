#Write a Python program that attempts to divide two numbers a = 10  b = 0
#and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error

a=10 
b=0

try:
    result=a/b
except ZeroDivisionError:
    print("Cannot Divide by Zero")
finally:
    print("Completed")