print("""TWO MORE QUESTIONS, BABY!

Think of something and I'll try to guess it!
""")

choice_1 = input("Question 1) Does it belong inside or outside or both? ").lower()
choice_2 = input("Question 2) Is it alive? ").lower()

if choice_1 == "inside" and choice_2 == "yes":
    print("Then what else could you be thinking of besides a houseplant?!?")
if choice_1 == "inside" and choice_2 == "no":
    print("Then what else could you be thinking of besides a shower curtain?!?")
if choice_1 == "outside" and choice_2 == "yes":
    print("Then what else could you be thinking of besides a bison?!?")
if choice_1 == "outside" and choice_2 == "no":
    print("Then what else could you be thinking of besides a billboard?!?")
if choice_1 == "both" and choice_2 == "yes":
    print("Then what else could you be thinking of besides a dog?!?")
if choice_1 == "both" and choice_2 == "no":
    print("Then what else could you be thinking of besides a cell phone?!?")
