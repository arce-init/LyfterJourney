my_list = []
target_number = int(input("Enter the number to search: "))
count = 0

for i in range(7):
    number = int(input("Enter a number: "))
    my_list.append(number)

for number in my_list:
    if number == target_number:
        count = count + 1

print(f"The number {target_number} appears {count} times")

