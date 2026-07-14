print("---- Gamer Level Classifier ----")

name = input("Enter your gamertag: ")
hours = int(input("How many hours have you been playing? "))
is_competitive = input("Do you play competitive?(yes/no): ")

if hours < 10:
    category = "Beginner 🟢"
    message = "Welcome to the gaming world!"
elif hours < 50:
    category = "Casual 🔵"
    message = "You're getting the hang of it."
elif hours < 200:
    category = "Gamer 🟣"  
    message = "You definitely know what you're doing."
elif hours >= 200 and is_competitive == "yes":
    category = "Pro 🔴"
    message = "You are a living legend"
else:
    category = "Gamer 🟣"
    message = "You have the experience, but not quite for competitive."

print(f"{name}, your category is: {category}")
print(message)