import random
random_num = random.randrange(1, 101)
user_guess = int(input("I'm thinking of a number between 1-100. Try to guess it. "))

if random_num == user_guess:
    print("You guessed it! What are the odds?!?")
    # The odds of guessing the same number is 1/100.
elif user_guess > random_num:
    print(f"Sorry, you are too high. I was thinking of {random_num}.")
elif user_guess < random_num:
    print(f"Sorry, you are too low. I was thinking of {random_num}.")
else:
    print("Your input is invalid.")

