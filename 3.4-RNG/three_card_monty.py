import random

random_num = random.randrange(1, 4)
print("You slide up to Fast Eddie's card table and plop down your cash.\nHe glances at you out of the corner of his eye and starts shuffling.\nHe lays down three cards.\n")
user_guess = int(input("""Which one is the ace?

	##  ##  ##
	##  ##  ##
	1   2   3

"""))

if user_guess == random_num:
    print("\nYou nailed it! Fast Eddie reluctantly hands over your winnings, scowling.")
else:
    print(f"\nHa! Fast Eddie wins again! The ace was card number {random_num}.")

if random_num == 1:
    print("""
    AA  ##  ##
	AA  ##  ##
	1   2   3
    """)
elif random_num == 2:
    print("""
    ##  AA  ##
	##  AA  ##
	1   2   3
    """)
else:
    print("""
    ##  ##  AA
	##  ##  AA
	1   2   3
    """)
