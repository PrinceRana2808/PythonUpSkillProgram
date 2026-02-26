from functools import wraps

def cache(func):
    cached_results = {}   # dictionary to store previous results

    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print("Returning cached result...")
            return cached_results[args]
        
        result = func(*args)
        cached_results[args] = result
        return result
    
    return wrapper


@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x


print(expensive_computation(5))
print(expensive_computation(5))