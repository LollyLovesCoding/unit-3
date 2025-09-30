import random

random_num = random.randrange(1, 11)
user_guess = int(input("Your guess: "))

if random_num == user_guess:
    print(f"That's right!  My secret number was {random_num}!")
else:
    print(f"Sorry, but I was really thinking of {random_num}.")
