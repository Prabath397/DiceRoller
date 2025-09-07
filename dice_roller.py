# Dice Roller 🎲

import random

print("🎲 Welcome to Dice Roller!")

while True:
    num_dice = int(input("How many dice do you want to roll? "))
    sides = int(input("How many sides should each die have? "))

    results = [random.randint(1, sides) for _ in range(num_dice)]
    print(f"Results: {results}")

    again = input("Roll again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye! 👋")
        break
