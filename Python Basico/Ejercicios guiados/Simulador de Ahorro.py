print("---- Savings Simulator ----")

name = input("Enter your name: ")
monthly_savings = float(input("How many dollars do you save per month? "))
months = int(input("How many months you want to simulate? "))
total = 0

for month in range(1, months + 1):
    total = total + monthly_savings
    print(f"Month {month}: total accumulated = {total}")

print(f"{name}, in {months} you will have saved: {total}")
