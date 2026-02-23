#Task: Ask the user to enter their age and check if they are eligible to vote based on their age.

age=input("Enter your age:")

if int(age)>18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")