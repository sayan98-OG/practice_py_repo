import random

list = [1,-1,0]

computer = random.choice(list)

dict = {1: 'Gun', -1: 'Water', 0: 'snake'}


us = input('Enter Your choice (s/w/g): ')
dictrev = {'g': 1, 'w': -1, 's': 0}
user = dictrev[us]
print(f'Computer have chosen {dict[computer]}')
print(f'User choice is {dict[dictrev[us]]}')

if user==computer:
    print ('The game is draw')
else:
    if computer==1 and user==-1:
        print ('You loose , Computer wins!!')
    elif computer==1 and user ==0:
        print ('You win!!')
    elif computer==0 and user ==1:
        print ('You win!!')
    elif computer==0 and user ==-1:
        print ('You loose , Computer wins!!')
    elif computer==-1 and user ==0:
        print ('You win!!')
    elif computer==-1 and user ==1:
        print ('You loose , Computer wins!!')

print('\nPlay again')
