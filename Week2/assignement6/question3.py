#Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.

from functools import wraps

def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x < 0:
            raise ValueError("Input must be a positive number")
        return func(x)
    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5


print(square_root(9)) 
print(square_root(-4)) 