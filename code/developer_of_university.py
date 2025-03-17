reg1 = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],
]
reg2 = [
  ["0", "Advanced Mechanics"],
  ["0", "Art History"],
  ["1", "Course 1"],
  ["1", "Course 2"],
  ["2", "Computer Architecture"],
  ["3", "Course 1"],
  ["3", "Course 2"],
  ["4", "Algorithms"]
]
reg3 = [
  ["23", "Software Design"], 
  ["3", "Advanced Mechanics"], 
  ["2", "Art History"], 
  ["33", "Another"],
]
 
def create_combinations(reg :list):
    l = []
    for i in reg:
        l.append(i[0])

    l = list(set(l))
    comb = []
    for i in l:
        for j in range(l.index(i)+1,len(l)):
            comb.append(f'{i},{l[j]}')

    return comb        



def create_dict(reg :list):
    comb = create_combinations(reg)
    dic = {}
    for i in reg:
        for j in comb:
            if i[0] in j:
                dic.setdefault(j, []).append(i[1])

    for k,v in dic.items():
        v2 = [i for i in v if v.count(i)>1]            
        dic[k] = list(set(v2))
    return dic            

# print(create_dict(reg1))
print(create_dict(reg2))
# print(create_dict(reg3))
