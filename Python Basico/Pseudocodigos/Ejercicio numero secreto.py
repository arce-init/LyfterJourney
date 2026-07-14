import random
secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the secret number (1-10): "))
    if guess == secret_number:
        print("You have guessed!", secret_number)
        break
    else:
        print("Incorrect, try again.")