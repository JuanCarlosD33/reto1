import random as rand

cont = 0
num = 0
ran = rand.randint(1, 10)

print("Guess a number between 1 and 10")

while num != ran:

    cont += 1

    num = input(f"Enter guess #{cont}: ")

    if num.isdigit():

        num = int(num)

        if num < ran:

            print("Your guess is too low, try again!")

        elif num > ran:

            print("Your guess is too high, try again!")
    
    else:

        print("Numbers only, please!")
else:

    print(f"You guessed it in {cont} tries!")