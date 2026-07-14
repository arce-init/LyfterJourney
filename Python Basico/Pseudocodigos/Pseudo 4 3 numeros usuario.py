first_number = int(input("Type your first number: "))
second_number = int(input("Type your second number: "))
third_number = int(input("Type your third number: "))
temp = 30

if (first_number == 30 or second_number == 30 or third_number == 30) or (first_number + second_number + third_number == 30):
    print("Correct!")
else:
    print("Incorrect!")