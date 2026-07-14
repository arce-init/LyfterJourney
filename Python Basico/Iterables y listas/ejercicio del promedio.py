my_list = []
for i in range(5):
    number = int(input("Enter 5 numbers: "))
    my_list.append(number)

total = 0
for number in my_list:
    total = total + number
average = total / len(my_list)

new_list= []
for number in my_list:
    if number > average:
        new_list.append(number)

print(f"Average: {average}")
print(f"New list: {new_list}")

