import time
from collections import namedtuple

# Q1. Object Modeling & Core OOP

class User:
    active_users = 0   # class level attribute
    def __init__(self, name, email):
        self.name = name
        self.email = email 
        User.active_users += 1
    def role(self):
        return "Generic User"
    def __str__(self):
        return f"User(name={self.name}, email={self.email})"


class Admin(User):
    def role(self):
        return "Admin"
    def perform_action(self):
        print(f"{self.name} can manage the system.")


class Customer(User):
    def role(self):
        return "Customer"
    def perform_action(self):
        print(f"{self.name} can place orders.")

# Q2. Advanced Class Construction

class UserFactory:
    @classmethod
    def from_string(cls, data):
        name, email = data.split(",")
        return User(name.strip(), email.strip())
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email


# Q3. Deep Usage of Special Methods

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
   
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"
    
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"


    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __call__(self, discount):
        new_price = self.price - discount
        return f"Discounted price: {new_price}"


# Q4. Decorator Driven Behavior

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end-start:.5f} seconds")
        print("-"*40)
        return result
    return wrapper

@log_execution
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Q5. Generator Based Data Streaming

class DataStreamer:
    def __init__(self, data):
        self.data = data
    def stream_data(self):
        for item in self.data:
            processed = item * 2
            yield processed


# Q6. Immutable Data Modeling

Config = namedtuple("Config", ["host", "port", "debug"])
class ConfigManager:
    def __init__(self):
        self.configs = []
    def add_config(self, host, port, debug):
        config = Config(host, port, debug)
        self.configs.append(config)
    def get_configs(self):
        return self.configs


# Q7. Loop Else Control Flow

def search_user(users, target):
    for user in users:
        if user.name == target:
            print(f"User found: {user.name}")
            break
    else:
        print("User not found")


# Q8. Module Execution Boundary

def show_users(users):
    for u in users:
        print(f"{u.name} - {u.role()}")

# Q9. Cross Cutting Decorators


def timing_decorator(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end-start:.5f} seconds")
        return result
    return wrapper

def permission_required(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.role() != role:
                print("Permission Denied")
                return
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


class SecureSystem:
    @permission_required("Admin")
    def shutdown(user):
        print(f"{user.name} shut down the system.")


# Q10. System Level Integration

@timing_decorator
def run_stream():
    data = range(5)
    streamer = DataStreamer(data)
    for value in streamer.stream_data():
        print(f"Streamed value: {value}")


def main():
    print("\n===== USER CREATION =====")

    admin = Admin("Prince", "prince@email.com")
    customer = Customer("Rahul", "rahul@email.com")

    users = [admin, customer]

    show_users(users)

    print(f"Active Users: {User.active_users}")


    print("\n===== CLASSMETHOD & STATICMETHOD =====")

    u = UserFactory.from_string("Amit, amit@email.com")

    print(u)

    print("Valid Email:", UserFactory.validate_email(u.email))


    print("\n===== SPECIAL METHODS =====")

    p1 = Product("Laptop", 1000)
    p2 = Product("Phone", 800)

    print(p1)
    print(repr(p1))

    print("Name length:", len(p1))

    print("Price comparison:", p1 > p2)

    print(p1(100))


    print("\n===== GENERATOR STREAM =====")

    run_stream()


    print("\n===== IMMUTABLE CONFIG =====")

    manager = ConfigManager()

    manager.add_config("localhost", 8000, True)

    for c in manager.get_configs():
        print(c)


    print("\n===== LOOP ELSE SEARCH =====")

    search_user(users, "Prince")
    search_user(users, "Amit")


    print("\n===== PERMISSION DECORATOR =====")

    SecureSystem.shutdown(admin)
    SecureSystem.shutdown(customer)


if __name__ == "__main__":
    main()