first_value = int(input('First Number: '))
second_value = int(input('Second number: '))
sum = first_value + second_value
print("Sum: " + str(sum))

#/////////////////////////////

numeric_value = '7'
print(numeric_value.isnumeric())

string_value = 'Bob'
print(string_value.isnumeric())

#/////////////////////////////

first_value = input('First Number: ')

if first_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

second_value = input('Second Number: ')

if second_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))

#/////////////////////////////

first_value = input('First Number: ')
second_value = input('Second Number: ')

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print('Please enter numbers only.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))

#/////////////////////////////

#/////////////////////////////

# Function	    Purpose
# isalnum()	    Ensures that the string has no special characters, such as %, $, #, @, or !.
# isalpha()	    Ensures that the string contains only letters of the alphabet.
# isdecimal()	Ensures that the string contains only decimal values (numbers).
# istitle()	    Ensures that the string follows the rules of capitalization (as in a sentence).
# isupper()	    Ensures that the string contains only uppercase letters.
# islower()	    Ensures that the string contains only lowercase letters.

#/////////////////////////////