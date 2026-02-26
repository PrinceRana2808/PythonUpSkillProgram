#Correct this below code with appropriate exception handlings. And finally print “Execution completed”

def safe_divide(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        print("Cannot divide by zero")
        result = None

    except TypeError:
        print("Invalid type. Please provide numbers only.")
        result = None

    else:
        print(f"Result: {result}")

    finally:
        print("Execution completed")


safe_divide(1, 0)
safe_divide(1, "a")