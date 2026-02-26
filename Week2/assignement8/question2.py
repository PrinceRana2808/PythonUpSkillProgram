#Write a Python program to count the number of words in a file named words.txt

with open("sample.txt","r") as file:
    content=file.read()
    word_count=content.split()
    count=len(word_count)

print(count)