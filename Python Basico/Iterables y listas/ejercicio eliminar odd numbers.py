my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in my_list [:]:
    if number % 2 != 0:
        my_list.remove(number)
print(my_list)