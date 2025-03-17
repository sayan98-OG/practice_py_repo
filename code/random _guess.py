from random import randint

cg = randint(1,20)
print(cg)

ug = int(input('Enter a guess'))
guess =1
while cg!=ug:
    guess += 1 
    if cg<ug:
        ug = int(input('guess a smaller number'))
    else :
        ug = int(input('guess a greater number'))

print(f'You guessed the correct number', f'\n number of guesses needed {guess}'  )

