def toatreasureroom(ins :list, treroom :list):
    lst = set()

    for i in ins:
        if i[1] in treroom:
            lst.add(i[0])

    return list(lst)

def fromtworoom(ins :list):
    lst = []
    roomto = {}
    for i in ins:
        if i[0] != i[1]:
            roomto.setdefault(i[1], []).append(i[0])

    for key,value in roomto.items():
        k = key
        v = value
        if len(v)>=2:
            lst.append(k)

    return lst

def filter_rooms(ins :list, treroom: list):
    c1=toatreasureroom(ins,treroom)
    c2=fromtworoom(ins)
    fnl = [i for i in c1 if i in c2]
    return fnl

instructions_1 = [ ["jasmin", "tulip"],["lily", "tulip"],["tulip", "tulip"], ["rose", "rose"],["violet", "rose"], ["sunflower", "violet"],["daisy", "violet"],["iris", "violet"]]
treasure_rooms_1 = ["lily", "tulip", "violet", "rose"]

instructions_2 = [ 
    ["jasmin", "tulip"],
    ["lily", "tulip"],
    ["tulip", "violet"],
    ["violet", "violet"]       
]
treasure_rooms_2 = ["lily", "jasmin", "violet"]  
 
treasure_rooms_3 = ["violet"]


print(filter_rooms(instructions_2,treasure_rooms_3))
print(filter_rooms(instructions_1,treasure_rooms_1))
print(filter_rooms(instructions_1,treasure_rooms_2))
