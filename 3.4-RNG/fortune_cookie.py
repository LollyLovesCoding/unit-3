import random

random_num = random.randrange(1, 7)
if random_num == 1:
    print('Fortune cookie says: "You will find happiness with a new love."')
elif random_num == 2:
    print('Fortune cookie says: "Keep your friends close and your enemies closer."')
elif random_num == 3:
    print('Fortune cookie says: "Stick with your wife."')
elif random_num == 4:
    print('Fortune cookie says: "You will find that lost item one day."')
elif random_num == 5:
    print('Fortune cookie says: "Good luck in your future endeavors!"')
else:
    print('Fortune cookie says: "I give you my full blessing"')

num1 = random.randrange(1, 55)
num2 = random.randrange(1, 55)
num3 = random.randrange(1, 55)
num4 = random.randrange(1, 55)
num5 = random.randrange(1, 55)
num6 = random.randrange(1, 55)

print(f"{num1} - {num2} - {num3} - {num4} - {num5} - {num6}")
