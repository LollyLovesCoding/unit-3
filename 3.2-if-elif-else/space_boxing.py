earth_weight = int(input("Please enter your current earth weight: "))
print("""I have information for the following planets:
    1. Venus   2. Mars    3. Jupiter
    4. Saturn  5. Uranus  6. Neptune
""")

planet_visiting = int(input("Which planet are you visiting? "))

if planet_visiting == 1:
    print(f"Your weight will be {earth_weight * 0.78} pounds on that planet.")
elif planet_visiting == 2:
    print(f"Your weight will be {earth_weight * 0.39} pounds on that planet.")
elif planet_visiting == 3:
    print(f"Your weight will be {earth_weight * 2.65} pounds on that planet.")
elif planet_visiting == 4:
    print(f"Your weight will be {earth_weight * 1.17} pounds on that planet.")
elif planet_visiting == 5:
    print(f"Your weight will be {earth_weight * 1.05} pounds on that planet.")
elif planet_visiting == 6:
    print(f"Your weight will be {earth_weight * 1.23} pounds on that planet.")
else:
    print("Your input is invalid.")
