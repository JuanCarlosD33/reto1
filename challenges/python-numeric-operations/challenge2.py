print("Simple calculator!")

First_number = input("First number? ")

Operation = input("Operation? ")

Second_number = input("Second number? ")

if First_number.isnumeric() == True and Second_number.isnumeric() == True:

    First_number = float(First_number)
    Second_number = float(Second_number)

    if Operation == '+':

        resul = First_number + Second_number
    
    elif Operation == '-':

        resul = First_number - Second_number
        
    elif Operation == '*':

        resul = First_number * Second_number
        
    elif Operation == '/':

        resul = First_number / Second_number
        
    elif Operation == '+':

        resul = First_number * Second_number
        
    elif Operation == '**':

        resul = First_number ** Second_number
        
    elif Operation == '%':

        resul = First_number % Second_number

    else:

        print("Operation not recognized.")
        exit()

else:

    print("Please input a number.")
    exit()


print(f"Product of {First_number} {Operation} {Second_number} equals {resul}")
