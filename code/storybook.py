# choices1_1 = [[3, 7, 8], [9, 4, 2]] => [[current_page, option_1, option_2], ...]
# The ending pages are also given in a sorted list:
 
# endings1 = [6, 15, 21, 30]


def readble(endings, choice, options ):
    visited = []
    start = 1
    choicepage = [item[0] for item in choice]
    optionlist1 = [item[1] for item in choice]
    optionlist2 = [item[2] for item in choice]
    
    while 1:
        # print(start)
        if start in endings:
            return start
        elif start in visited:
            return -1
        elif start in choicepage:
            visited.append(start)
            if options == 1:
                point = choicepage.index(start)
                start = optionlist1[point]
            elif options == 2:
                point = choicepage.index(start)
                start = optionlist2[point]    

        else:
            visited.append(start)
            start += 1

choices1_1 = [[3, 7, 8], [9, 4, 2]]
choices1_2 = [[3, 14, 2]]
choices1_3 = [[5, 11, 28], [9, 19, 29], [14, 16, 20], [18, 7, 22], [25, 6, 30]]
choices1_4 = [[2, 10, 15], [3, 4, 10], [4, 3, 15], [10, 3, 15]]
endings1 = [6, 15, 21, 30]

print(readble(endings1, choices1_1, 1))
print(readble(endings1, choices1_1, 2)) 
print(readble(endings1, choices1_2, 1)) 
print(readble(endings1, choices1_2, 2)) 
print(readble(endings1, choices1_3, 1)) 
print(readble(endings1, choices1_3, 2)) 
print(readble(endings1, choices1_4, 1)) 
print(readble(endings1, choices1_4, 2))  