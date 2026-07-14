my_list = [3, 5, 5, 9, -81, -75, -3, -54, 5, 6, 7, 22]
count = 0

for i in my_list:
    if i <= 0:
        count = count +1

if count == 0:
    print("All numbers are positive")
else:
    print(f"There is at least {count} negative number or zero")


