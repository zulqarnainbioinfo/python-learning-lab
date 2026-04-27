import random

print("---Guess The Random Number Game---")
print("Let's set your range!")
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
actual_min = min(start,end)
actual_max = max(start,end)
number = random.randint(actual_min,actual_max)

level = input("Enter your difficulty level (easy/hard): ").lower()
if level in ["e","easy"]:
    chances = 10
    level = "easy"
elif level in ["h","hard"]:
    chances = 3
    level = "hard"
else:
    print("Invalid choice, defaulting to easy.")
    chances = 10
    level = "easy"
print(f"Difficulty set to {level}. You have {chances} chances to guess the number!")

while chances > 0:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print(f"You won! The number is {number}")
        break
    elif guess > number:
        chances -= 1
        if chances > 0:
            print("Wrong, your guess is higher.")
            print(f"You have {chances} chances left.")
        else:
            print("That was your last chance!")
    elif guess < number:
        chances -= 1
        if chances > 0:
            print("Wrong, your guess is lower")
            print(f"You have {chances} chances left.")
        else:
            print("That was your last chance!")
    else:
        print("Please enter a valid number.")

if chances == 0:
    print(f"Game Over! The correct number was {number}.")
