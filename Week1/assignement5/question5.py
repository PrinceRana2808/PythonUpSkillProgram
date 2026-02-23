#Write a Python function that takes a list and returns a new list with distinct and sorted elements from the first list.
#a = [4,1,2,3,3,1,3,4,5,1,7]
#Output = [1,2,3,4,5,7]

a=[4,1,2,3,3,1,3,4,5,1,7]
b=sorted(a)
c=set()
for val in range(len(b)):
    c.add(a[val])

print(c)