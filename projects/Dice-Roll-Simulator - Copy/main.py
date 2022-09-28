import random

while True:
    print(" 1. roll the dice \n  2. exit  ")
    user = int(input("what you want to do\n"))
    if user == 1:
        for x in range(3):
            number = random.randint(1, 20)
            print("dice " + str(x+1) + " is " + str(number)) 
    else:
        break
 