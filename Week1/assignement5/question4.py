#. Write a Python function that takes two parameters as lists and to sum all the numbers in a list. 

a =[8, 2, 3, 0, 7]
b =[3, -2, 5, 1]
a.extend(b)
sum=0
for val in range(len(a)):
    sum+=a[val]
print(sum)
