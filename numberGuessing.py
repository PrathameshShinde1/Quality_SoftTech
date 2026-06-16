import random

ran = int(input("Enter the maximum range: "))

secret_number = random.randint(1, ran)

while True:
    guess = int(input(f"Guess a number between 1 and {ran}: "))

    if guess == secret_number:
        print(" Your guess is correct!")
        break
    elif guess < secret_number:
        print("No, Increase your guess number.")
    else:
        print("No, Decrease your guess number.")