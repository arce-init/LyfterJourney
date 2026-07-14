def get_name():
    name = ""
    try:
        name = input("Enter your name: ")
        if name.isdigit():
            raise ValueError("The name can't be a number")
    except Exception as error:
        print(error)
    return name

def get_age():
    age = 0
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid number")
    return age

def show_greeting(name, age):
    if name and not name.isdigit():
        print(f"Hello {name}, your age is {age}")

def main():
    name = get_name()
    age = get_age()
    show_greeting(name, age)

main()