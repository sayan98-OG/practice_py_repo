def add_space(lis):
    l=lis
    l_updt =[]
    for g in l:
        item = g
        new_item = ''


        for i, letter in enumerate(item):
            if letter.isupper():
                new_item += ' '

            new_item += letter

        l_updt.append(new_item)

    return l_updt    

n = int(input("Enter a number of elements: "))
i=1
a=[]
while i<=n:
    b = input("Enter a  elements: ")
    a.append(b)
    i += 1
print(add_space(a))


#['saYan', 'ayanTiKa', 'zUko', 'kataRa']
#['sa Yan', 'ayan Ti Ka', 'z Uko', 'kata Ra']