import random

chances=0



number=random.randint(1,10)


while chances < 5:
    guess=int(input("Guess a Number between 1 and 10:"))
    if guess == number:
        print("YOU WIN!!")
        break

    elif guess > number:
        print("GUESS LOWER,TRY AGAIN")

    else:
        print("GUESS HIGHER,TRY AGAIN")
            
    chances+=1

if not chances < 5:
    print("YOU LOSE!! THE NUMBER IS ",number)
    