name = input("Hey, what's your name? ")
age = int(input(f"Ok, {name}, how old are you? "))

if age < 16:
    print(f"You can't drive, {name}.")

if age < 18:
    print(f"You can't vote, {name}.")

if age < 21:
    print(f"You can't rent a car, {name}.")

if age >= 21:
    print(f"You can do anything that's legal, {name}.")

# IPO Model
# Input: age <= 15; output: Can't drive, can't vote, can't rent a car
# Input: age <= 17; output: Can't vote, can't rent a car
# Input: age <= 20; output: Can't rent a car
# Input: age >= 21; output: Do anything that's legal
