name = input("Hey, what's your name? (Sorry, I keep forgetting): ")
age = int(input(f"Ok, {name}, how old are you? "))

if age < 16:
    print(f"You can't drive, {name}.")

elif age < 18:
    print(f"You can't vote, {name}.")

elif age < 21:
    print(f"You can't rent a car, {name}.")

else:
    print(f"You can do anything that's legal, {name}.")
