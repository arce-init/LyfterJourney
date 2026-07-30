from datetime import datetime
from functools import wraps

def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Parameter {arg} is not a number")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"Parameter {key}={value} is not a number")
        return func(*args, **kwargs)
    return wrapper

from datetime import datetime

def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_str = ", ".join(str(arg) for arg in args)
        timestamp = datetime.now()
        print(f"func:{func.__name__} - args: {args_str} - [{timestamp}] - Result: {result}")
        return result
    return wrapper

@log_call
@validate_numbers
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(f"Result {result}")