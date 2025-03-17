
m1 = int(input('enter the marks: '))
m3 = int(input('enter the marks: '))
m2 = int(input('enter the marks: '))

print(m1+m2+m3)

if ((m1+m2+m3)>=120):
    if (m1>=33 and m2>33 and m3>= 33):
        print('Student is passed')
    else :
        print('Student is failed')
else :
    print('Student is failed')