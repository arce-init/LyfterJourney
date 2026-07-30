def admin_only(func):
    def wrapper(user, *args):
        if user.role != "Admin":
            raise ValueError("You are not allowed to run this function...")
        func(user, args)
    return wrapper

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Parameter {arg} is not a number")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"Parameter {key}={value} is not a number")
        return func(*args, **kwargs)
    return wrapper

@validate_numbers
def add(a, b):
    return a + b

print(add(3, 5))
print(add(3, "5"))

@validate_numbers
def multiply(a, b=1):
    return a * b

print(multiply(4, b=2))
print(multiply(4, b="two"))