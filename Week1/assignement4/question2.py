#Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”

string=input("Enter a String:")
temp_str=""
for ch in string:
    temp_str = ch + temp_str
if string == temp_str:
    print("String is pallindrome")
else:
    print("String is not pallindrome")
