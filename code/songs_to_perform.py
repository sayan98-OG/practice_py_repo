def setheirarchy():
    hierarchy = []
    pitch = 'CDEFGAB'
    o = 0 

    while o < 8:
        for i in pitch:
            hierarchy.append(i+str(o))
        o += 1            
    return hierarchy

def prepostcompare(song :list, lp, hp):
    h=setheirarchy()
    f=0
    for i in song:
        if h.index(i)>=h.index(lp) and h.index(i)<=h.index(hp):
            pass
        else:
            f+=1

    if f>0:
        return False
    else:
        return True
    

def compare(song, low, high):
    songoctave = song[1]
    lowoctave = low[1]
    highoctave = high[1]
    sp = song[0]
    lp = low[0]
    hp = high[0]
    hy = 'CDEFGAB'
    s = hy.index(sp)
    l = hy.index(lp)
    h = hy.index(hp)
    if songoctave<highoctave and songoctave>lowoctave:
        return 1
    elif songoctave<lowoctave:
        return 0    
    elif songoctave>highoctave:
        return 0 
    elif songoctave==highoctave==lowoctave:
        if s>=l and s<=h:
            return 1
        else :
            return 0
    elif songoctave == highoctave:
        if s<=h:
            return 1
        else :
            return 0
    elif songoctave == lowoctave:
        if s>=l:
            return 1
        else:
            return 0
        
def singable(l:list, low, high):
    out = []
    for i in l:
        out.append(compare(i, low, high))

    if 0 in out:
        return False
    else :
        return True      
    

song1 = ["F4", "B4", "C5"]
song2 = ["C3", "E3", "G3", "C4", "E4", "G4", "C5"]
song3 = [ "B4", "F5", "B5" ]
song4 = ["B4", "E4", "G4", "G4", "A4", "B4", "E4", "B4", "E4", "G4", "G4", "A4", "C5", "B4", "E5", "G4", "G4", "A4", "B4", "C5", "D5", "C5", "B4", "C5", "E5", "D5", "C5", "C5", "B4", "B4", "E5", "E4", "G4", "G4", "A4", "B4", "B4", "B4", "C5", "E5", "A5", "E5", "C5", "A4", "E5", "D5", "C5", "B4"]
song5 = [ "F4" ]

print(prepostcompare(song1, "F4", "C5"))
print(prepostcompare(song1, "A4", "C5")) 
print(prepostcompare(song2, "B2", "C5"))
print(prepostcompare(song2, "C3", "B4")) 
print(prepostcompare(song3, "B4", "B5"))
print(prepostcompare(song3, "B4", "C5")) 
print(prepostcompare(song4, "D4", "A5"))
print(prepostcompare(song4, "D4", "G5")) 
print(prepostcompare(song4, "D4", "C6"))
print(prepostcompare(song4, "F4", "C6")) 
print(prepostcompare(song5, "D4", "E4")) 

print(singable(song1, "F4", "C5"))
print(singable(song1, "A4", "C5")) 
print(singable(song2, "B2", "C5"))
print(singable(song2, "C3", "B4")) 
print(singable(song3, "B4", "B5"))
print(singable(song3, "B4", "C5")) 
print(singable(song4, "D4", "A5"))
print(singable(song4, "D4", "G5")) 
print(singable(song4, "D4", "C6"))
print(singable(song4, "F4", "C6")) 
print(singable(song5, "D4", "E4")) 