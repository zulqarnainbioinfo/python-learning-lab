import random

# Title
title_messages = [
    "--- WELCOME TO: THE NUMBER GUESSING CHALLENGE ---",
    "=== GUESS THE RANDOM NUMBER ===",
    "*** Welcome, Player! Can you guess the Secret Number? ***",
    "+++ THE GREAT RANDOM NUMBER HUNT +++",
    "~~~ Prepare to test your luck in: GUESS THE RANDOM NUMBER ~~~"
]
print(random.choice(title_messages))

# Random number and its range
range_setup_prompts = [
    "Would you like to set a custom range for the secret number? (yes/no): ",
    "Do you want to define your own range or use the default (1-20)? (yes/no): ",
    "Custom range mode? (yes/no): ",
    "Shall we customize the range of numbers? (yes/no): ",
    "Ready to pick your own boundaries? Enter 'yes' to customize or 'no' for default: "
]
start_prompts = ["Enter the starting number: ", "Pick the minimum value: ", "What's the lower bound? ", "Enter your start number: ", "Lowest number in your range: "]
end_prompts = ["Enter the ending number: ", "Pick the maximum value: ", "What's the upper bound? ", "Enter your end number: ", "Highest number in your range: "]
default_range_messages = [
    "Using default range: 1 to 20.",
    "No custom range selected. Playing within 1 to 20.",
    "Defaulting to a standard 1-20 range.",
    "Setting range to the classic 1-20.",
    "Default range locked in: 1 to 20."
]
choice = input(random.choice(range_setup_prompts)).lower()
if choice == "yes":
    start = int(input(random.choice(start_prompts)))
    end = int(input(random.choice(end_prompts)))
    actual_min = min(start,end)
    actual_max = max(start,end)
else:
    actual_min = 1
    actual_max = 20
    print(random.choice(default_range_messages))
number = random.randint(actual_min,actual_max)

# Difficulty Level
difficulty_prompts = [
    "Choose your difficulty level (easy/hard): ",
    "How hard should this be? Type 'easy' or 'hard': ",
    "Set your challenge: easy or hard? ",
    "Difficulty setting? (easy/hard): ",
    "Ready for the test? Pick 'easy' (10 tries) or 'hard' (3 tries): "
]
invalid_difficulty_messages = [
    "That difficulty doesn't exist! Defaulting to easy.",
    "Invalid choice. Let's start with easy mode.",
    "Couldn't recognize that level, so we'll stick to easy.",
    "Unknown difficulty. Defaulting to easy mode for now.",
    "Invalid input! Defaulting to easy."
]
level = input(random.choice(difficulty_prompts)).lower()
if level in ["e","easy"]:
    chances = 10
    level = "easy"
elif level in ["h","hard"]:
    chances = 3
    level = "hard"
else:
    print(random.choice(invalid_difficulty_messages))
    chances = 10
    level = "easy"

# Random messages lists
difficulty_messages = [
    f"Difficulty locked to '{level}'. You have {chances} attempts to win!",
    f"Challenge accepted! Mode: {level.upper()} | Chances: {chances}",
    f"Setting difficulty to {level}... You get {chances} tries to find the number.",
    f"Game ready! You are playing on {level} mode with {chances} chances.",
    f"Level: {level.capitalize()}. You have exactly {chances} chances to get it right!"
]
print(random.choice(difficulty_messages))

lose_messages = [
    f"Game over! The correct number was {number}.",
    f"Oh no! You didn't guess {number}. Better luck next time!",
    f"You lose. The secret number was {number}.",
    f"Out of attempts! The number you were looking for was {number}.",
    f"Defeat! The number has vanished—it was {number}."
]
win_messages = [
    f"Spot on! {number} was the number!",
    f"Incredible! You guessed {number} perfectly.",
    f"Winner winner! You nailed it, the number was {number}.",
    f"You've got a sharp intuition! It was indeed {number}.",
    f"Jackpot! You correctly identified {number}."
]
higher_hints = [
    "Go higher!",
    "Your guess is too low, try a larger number.",
    "The target number is lurking above your current guess.",
    "Aim higher! The secret number is greater.",
    "Not quite—try adding more to your guess."
]
lower_hints = [
    "Too high! Try a smaller number.",
    "Go lower! The target is beneath your guess.",
    "You're overshooting it. Try something smaller.",
    "The secret number is lower than that.",
    "Ease off! The target is smaller than your current guess."
]
last_chance_messages = [
    "This is it—your final chance!",
    "One last attempt! Make it count.",
    "Down to the wire! This is your last guess.",
    "Make this last one a good one!",
    "It all comes down to this final try."
]
invalid_input_messages = [
    "That doesn't look like a number! Please try again.",
    "Oops! Please enter a valid numerical digit.",
    "I'm looking for a number, not letters! Give it another go.",
    "Invalid input. Let's stick to numbers, okay?",
    "Hmm, that's not a valid guess. Please type a number."
]
guess_prompts = [
    "What is your guess? ",
    "Take a shot! Enter your number: ",
    "Give me your best guess: ",
    "Enter a number: ",
    "Make your move! What is the secret number? "
]
victory_messages = [
    "VICTORY! You managed to crack the code!",
    "CONGRATULATIONS! You guessed the secret number like a pro.",
    "SUCCESS! You've conquered the challenge!",
    "BRAVO! Your intuition is spot on.",
    "CHAMPION! You found the number in time!"
]
closing_messages = [
    "--- Thanks for playing! Hope you had fun. ---",
    "=== Session Ended. Come back soon for another round! ===",
    "*** Thanks for challenging your brain with us today! ***",
    "+++ Hope you enjoyed the game. Goodbye! +++",
    "~~~ Game closed. See you next time! ~~~"
]

# While Loop
while chances > 0:
    try:
        remaining_messages = [
    f"Not quite. You have {chances} chances remaining.",
    f"Keep trying! {chances} attempts left.",
    f"Close, but no. {chances} chances left to go.",
    f"Wrong guess, but don't give up! {chances} chances remain.",
    f"Still {chances} chances left in the tank."
]
        guess = int(input(random.choice(guess_prompts)))
        if guess == number:
            print(random.choice(win_messages))
            break
        elif guess > number:
            chances -= 1
            if chances > 0:
                print(random.choice(lower_hints))
                print(random.choice(remaining_messages))
            else:
                print(random.choice(last_chance_messages))
        elif guess < number:
            chances -= 1
            if chances > 0:
                print(random.choice(higher_hints))
                print(random.choice(remaining_messages))
            else:
                print(random.choice(last_chance_messages))
    except ValueError:
        print(random.choice(invalid_input_messages))

# Final Exit
if chances > 0:
    print(random.choice(victory_messages))
else:
    print(random.choice(lose_messages))
print(random.choice(closing_messages))
