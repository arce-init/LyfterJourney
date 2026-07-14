name = input("Enter your name: ")
lastname = input("Enter your last name: ")
age = int(input("Enter your age: "))

if age <= 2:
    print(f"{name} {lastname}, You are a baby")
elif 3 <= age <= 8:
    print(f"{name} {lastname}, You are a Kid")
elif 9 <= age <= 12:
    print(f"{name} {lastname}, You are a Preteen")
elif 13 <= age <= 18:
    print(f"{name} {lastname}, You are a teenager")
elif 19 <= age <= 29:
    print(f"{name} {lastname}, You are a Young Adult")
elif 30 <= age <= 59:
    print(f"{name} {lastname}, You are an Adult")
elif age >= 60:
    print(f"{name} {lastname}, You are an Elderly person")
