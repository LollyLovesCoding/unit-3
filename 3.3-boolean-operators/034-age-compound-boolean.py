name = input("Hey, what's your name? ")
age = int(input(f"Ok, {name}, how old are you? "))

if age < 16:
    print(f"You can't drive, {name}.")

if 16 <= age and age <= 17:
    print(f"You can drive but not vote, {name}.")

if 18 <= age and age <= 24:
    print(f"You can vote but not rent a car, {name}.")

if age >= 25:
    print(f"You can do pretty much anything, {name}.")
