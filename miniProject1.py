import random

secret = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Your guess is correct")
elif guess > secret:
    print("Too high")
else:
    print("Too Low")