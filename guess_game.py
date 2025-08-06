import random

randint = random.randint(1,100)
win = True
count = 1
userguess = int(input("enter a number"))
while win:
    
    if randint == userguess:
        print("You guessed Congratulation!")
        print("You guesses num", userguess, "in", count, "times")
        win = False
    elif randint > userguess:
        print("your num", userguess, "is smaller")
        userguess = int(input("enter a another number"))
        count += 1 
    elif userguess > randint:
        print("your num", userguess, "is greater")
        userguess = int(input("enter a another number"))
        count += 1

print("---GAME OVER---")