import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("Congratulations! You guessed the number.")
else:
    print("Sorry, the number was", number)
