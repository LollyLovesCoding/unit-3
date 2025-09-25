questions_correct = 0
start = input("Are you ready for a quiz? (yes/no): ").lower()

if start == "yes":
    print("Okay, here it comes!")
    q1_answer = input("""Q1) What is the capital of Alaska?
	1) Melbourne
	2) Anchorage
	3) Juneau\n""")
    if q1_answer == "3":
        print("That's right!\n")
        questions_correct += 1
    else:
        print("Incorrect! The capital of Alaska is Juneau.\n")
    q2_answer = input("""Q2) In Python, the way you get keyboard input is the keyboard_input function.
	1) true
	2) false\n""")
    if q2_answer == "2":
        print("That's right!\n")
        questions_correct += 1
    else:
        print('Incorrect! In python, you would use the "input" function to get keyboard input.\n')
    q3_answer = input("""Q3) What is the result of 9 + 6 / 3?
	1) 5
	2) 11
	3) 15/3\n""")
    if q3_answer == "2":
        print("That's right!\n")
        questions_correct += 1
    else:
        print("Incorrect! The python terminal follows BEDMAS, so the correct answer should be 11.\n")
    print(f"Overall, you got {questions_correct} out of 3 correct.\nThanks for playing!")
