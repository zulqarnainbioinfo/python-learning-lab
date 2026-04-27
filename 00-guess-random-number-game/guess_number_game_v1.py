import random

number = random.randint(1,20)
print("---Guess The Random Number Game---")
print("1-20")

while True:
    guess = int(input("Enter a number: "))
    if guess == number:
        print(f"You won! The number is {number}")
        break
    elif guess > number:
        print("Wrong, your guess is higher.")
    elif guess < number:
        print("Wrong, your guess is lower")
    else:
        print("Please enter a valid number.")
