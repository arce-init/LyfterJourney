def convert_to_integer(list):
    print("Result: ")
    for element in list:
        result = 0
        try:
            result = int(element)
            print(f'"{element}" converted to {result}')
        except ValueError:
            print(f"Could not convert element: {element}")

def sum_values(list):
    total = 0
    for element in list:
        value = 0.0
        try:
            value = float(element)
            total = total + value
            print(f"{value} added successfully")
        except ValueError:
            print(f"Invalid element: {element}")
    print(f"Total sum: {total}")

my_list1 = ['4', 'hello', '10', '5.2']
convert_to_integer(my_list1)

my_list2 = ['10', 'apple', '5.5', '3','n/a']
sum_values(my_list2)