import random
random.seed(1) # Changing this number changes the numbers that stay the same
# The numbers for each run stayed the same!
# Games like Minecraft uses the concept of "seed" to generate a random world but save it so that the world will be the same everytime the user plays again.

x = random.randrange(10)  # 0-9
print(f"My random number is {x}.")
print()
print("Here are some random numbers from 1 to 4...")
# Changing random.randrange(1, 6) to random.randrange(1, 5) causes the new range of numbers to be 1-4 (1, 2, 3, 4)
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5), end=", ")
print(random.randrange(1, 5))

print()
print("Here are some random numbers from 1 to 100...")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()
print("Will these next two random number be the same?")
a = random.randrange(10)  # 0-9
b = random.randrange(10)

if a == b:
    print(f"Wow! Both numbers were {a}!")
else:
    print("The two random numbers were different. Not too surprising.")
