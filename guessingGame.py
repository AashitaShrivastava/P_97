import random
print("Number Guessing Game")
rand=random.randint(1,9)
print("Guess a number from 1-9")
chance=0

while chance<5:
    guess=int(input("enter your guess: "))
    if guess==rand:
        print("Congratulations you won!")
        break
    elif guess<rand:
        print("your guess is too low")
    else:
        print("your guess is to high")
    chance+=1
    
if not chance<5:
    print("You lose! The number is ",rand)