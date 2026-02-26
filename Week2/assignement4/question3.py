#Write a Python function that takes a list of strings as input and returns a tuple containing the 
# shortest and longest word from the list, in that order. If there are multiple words of the same 
# shortest or longest length, return the first shortest/longest word found.
#Output: ('kiwi', 'grapefruit')

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]

def find_word(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return (shortest, longest)

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]

result = find_word(words)
print(result)