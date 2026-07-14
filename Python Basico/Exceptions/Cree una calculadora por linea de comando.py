def show_menu(current_number):
    print(f"\nCurrent Number: {current_number}")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Erase")

def get_option():
    option = 0
    try:
        option = int(input("Select an option: "))
        if option not in [1, 2, 3, 4, 5]:
            raise ValueError()
    except Exception:
        print("Invalid option")
    return option

def get_number():
    number = 0.0
    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Invalid number")
    return number

def calculate(current_number, option, number):
    try:
        if option == 1:
            return current_number + number
        elif option == 2:
            return current_number - number
        elif option == 3:
            return current_number * number
        elif option == 4:
            if number == 0:
                raise ZeroDivisionError()
            return current_number / number
        elif option == 5:
            return 0
    except ZeroDivisionError:
        print("You can't divide by zero")
    return current_number

def main():
    current_number = 0
    while True:
        show_menu(current_number)
        option = get_option()
        if option == 0:
            continue 
        number = get_number()
        current_number = calculate(current_number, option, number)

main()