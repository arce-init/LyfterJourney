my_list = []
for i in range(5):
    number = int(input("Enter 5 numbers: "))
    my_list.append(number)

smallest = my_list[0]
for number in my_list:
    if number < smallest:
        smallest = number
print(f"The smallest number is {smallest}")

