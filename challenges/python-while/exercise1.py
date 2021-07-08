import random 

roll = 0
count = 0

while roll != 5:
  count = count + 1
  roll = random.randint(1, 5)
  print(roll)

print(f'It took {count} rolls to roll a 5!')

#////////////////////////////////////////////////////////////

roll2 = 0
count2 = 0

print('First person to roll a 5 wins!')
while roll2 != 5:
  
  name = input('Enter a name, or \'q\' to quit:  ' )
  if name == 'q':
    break
  
  count2 = count2 + 1
  roll2 = random.randint(1, 5)
  print(f'{name} rolled {roll2}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count2} times.')

#////////////////////////////////////////////

roll = 0
count = 0

print('First person to roll a 5 wins!')
while roll != 5:
  name = input('Enter a name, or \'q\' to quit:  ' )

  if name.strip() == '':
      continue

  if name.strip() == 'q':
      break
  
  count = count + 1
  roll = random.randint(1, 5)
  print(f'{name} rolled {roll}')
else:
    print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')