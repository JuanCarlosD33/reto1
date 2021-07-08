import random as rand

count = 0
num = 0
ran = rand.randint(1, 5)

while num != ran:
    
    count += 1

    num = input("Guess a number between 1 and 5: ")

    if num.isdigit() == False:

        continue
    else:

        num = int(num)

else:

    print(f"You guessed it in {count} tries!")