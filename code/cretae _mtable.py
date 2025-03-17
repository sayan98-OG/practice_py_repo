def createtable(int):
    for g in range (1,11):
        line=str(int)+'x'+str(g)+' : '+str(int*g)
        with open('table.txt','a') as g:
            g.write(f'{line}\n')

for i in range (2,21):
    createtable(i)
