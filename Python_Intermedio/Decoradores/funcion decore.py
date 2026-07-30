def decorator_name(func):
    def wrapper(parameters):
        func(parameters)
    return wrapper

def print_params_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Parameters: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

@print_params_and_result
def add(a, b):
    return a + b

add(3, 5)

@print_params_and_result
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alejandro", greeting="Hello")