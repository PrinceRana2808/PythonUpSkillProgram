#Find the first occurrence of a number in a list and stop further searching. 

numbers = [10, 20, 30, 40, 50]
search_for = 30

for num in range(len(numbers)):
    if(numbers[num]==search_for):
        print(f"Number found at index {num}")
        break

