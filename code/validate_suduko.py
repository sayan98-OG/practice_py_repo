def validaterowSoduku(l :list):
    n = len(l)
    flag = 0
    for i in l:
        test = i
        for g in range(1,n+1):
            if g in i:
                pass
            else :
                flag =+ 1


    if flag == 0:
        return True
    else :
        return False
    
def validatecolumnSoduku(l :list):
    n = len(l)
    flag = 0
    
    for i in range(n):
        tempcollst = [item[i] for item in l]
        for g in range(1,n+1):
            if g in tempcollst:
                pass
            else :
                flag =+ 1

    if flag == 0:
        return True
    else :
        return False 

def fnl(l :list):
    if validatecolumnSoduku(l) and validaterowSoduku(l):
        print(True) 
    else :
        print(False)      

grid1 = [[1,2,3,4],[2,1,4,3],[4,4,1,2],[3,4,2,1]]
fnl(grid1)