import random
def game():
    t = random.choice([10,20,30,40,50,60,70])
    return t 

with open('hiscore.txt') as f:
    hiscore = f.read()
    if hiscore=='':
        hiscore=0
    else :
        hiscore = int(hiscore)
        print(f'previous hiscore is {hiscore}')

with open('hiscore.txt','w') as q:
    nscore = game()
    print('your new score is ',nscore)
    if (nscore>hiscore):
        q.write(str(nscore))
    else:
        q.write(str(hiscore))   



     
