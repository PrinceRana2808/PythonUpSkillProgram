#Write a function that appends 1 to 1000 numbers to a list and add a decorator to that 
# function to calculate the start and end time. Calculate the total time taken and print.

import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Total Time Taken: {total_time} seconds")
        
        return result
    return wrapper
@calculate_time
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)
    return numbers


r=append_numbers()