print("WELCOME TO LILYANA'S TINY ADVENTURE!")

choice_1 = input('You are in a creepy house!  Would you like to go "upstairs" or into the "kitchen"? ').lower()

if choice_1 == "upstairs":
    choice_2 = input(
        'Upstairs you see a hallway. At the end of the hallway is the master "bedroom". There is also a "bathroom" off the hallway. Where would you like to go? ').lower()
    if choice_2 == "bedroom":
        choice_3 = input(
            'You are in a plush bedroom, with expensive-looking hardwood furniture. The bed is unmade. In the back of the room, the closet door is ajar. Would you like to open the door? ("yes" or "no") ').lower()
        if choice_3 == "yes":
            print("The closet starts glimmering with power, and you spot a chest full of treasure.")
        elif choice_3 == "no":
            print(
                "Well, then I guess you'll never know what was in there. Thanks for playing, I'm tired of making nested if statements.")
        else:
            print("Your input is invalid.")
    elif choice_2 == "bathroom":
        choice_3 = input('You find that the shower is open, do you take another step? ("yes" or "no") ').lower()
        if choice_3 == "yes":
            print("You open the curtains and see a ghost, which devours your soul... ")
        elif choice_3 == "no":
            print("Just as you were about to leave, a gust of wind sweeps you into the underworld... ")
        else:
            print("Your input is invalid.")
    else:
        print("Your input is invalid.")
elif choice_1 == "kitchen":
    choice_2 = input(
        'There is a long counter top with dirty dishes everywhere. Off to one side there is, as you would expect, a refrigerator. You may open the "refrigerator" or look in a "cabinet". ').lower()
    if choice_2 == "refrigerator":
        choice_3 = input(
            'Inside the refrigerator you see food and stuff. It looks pretty nasty. Would you like to eat some of the food? ("yes" or "no") ').lower()
        if choice_3 == "yes":
            print("You die of food poisoning... unfortunately.")
        elif choice_3 == "no":
            print("You die of starvation... eventually.")
        else:
            print("Your input is invalid")
    elif choice_2 == "cabinet":
        choice_3 = input(
            'You open the cabinet to a crowd of rats. They look pretty dangerous. "fight" or "flight"? ').lower()
        if choice_3 == "fight":
            print("You defeat the rats but sustain a bite from the king rat... which ultimately kills you.")
        elif choice_3 == "flight":
            print("The rats call their relatives and surround you... you can't run.")
        else:
            print("Your input is invalid.")
    else:
        print("Your input is invalid.")
else:
    print("Your input is invalid.")


