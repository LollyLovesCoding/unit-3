name = input("What's your last name? ").lower()

if name <= "carswell":
    print("You don't have to wait long.")
elif name <= "jones":
    print("That's not bad!")
elif name <= "smith":
    print("Looks like a bit of a wait.")
elif name <= "young":
    print("It's gonna be a while...")
elif name > "young":
    print("Not going anywhere for a while?")
