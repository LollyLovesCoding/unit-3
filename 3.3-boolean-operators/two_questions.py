print("TWO QUESTIONS!\nThink of an object, and I'll try to guess it.\n")

q1_answer = input("Question 1) Is it an animal, vegetable, or mineral? ").lower()
if q1_answer == "animal":
    q2_answer = input("Question 2) Is it bigger than a breadbox? (yes/no): ").lower()
    if q2_answer == "yes":
        print("My guess is that you are thinking of a moose.")
    elif q2_answer == "no":
        print("My guess is that you are thinking of a squirrel.")
    else:
        print("Your input is invalid.")
elif q1_answer == "vegetable":
    q2_answer = input("Question 2) Is it bigger than a breadbox? (yes/no): ").lower()
    if q2_answer == "yes":
        print("My guess is that you are thinking of a watermelon.")
    elif q2_answer == "no":
        print("My guess is that you are thinking of a carrot.")
    else:
        print("Your input is invalid.")
elif q1_answer == "mineral":
    q2_answer = input("Question 2) Is it bigger than a breadbox? (yes/no): ").lower()
    if q2_answer == "yes":
        print("My guess is that you are thinking of a camaro.")
    elif q2_answer == "no":
        print("My guess is that you are thinking of a paper clip.")
    else:
        print("Your input is invalid.")
else:
    print("Your input is invalid.")
