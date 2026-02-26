#Create a parameterised decorator retry that retries a function a specified number of times.
import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Total Execution Time: {end - start:.6f} seconds")
        return result
    return wrapper

@calculate_time
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)
    return numbers

append_numbers()