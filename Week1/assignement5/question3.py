#Write a function that takes one parameter as a string and reverse it and return.

def reverse_string(text):
    return ''.join(reversed(text))

text = input("Enter String that has to reversed: ")

reversed_str = reverse_string(text)
print(reversed_str)