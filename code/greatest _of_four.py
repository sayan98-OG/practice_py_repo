
a = int(input('enter a number - ', ))
b = int(input('enter a number - ', ))
c = int(input('enter a number - ', ))
d = int(input('enter a number - ', ))


if(a>=b and a>=c and a>=d):
    print('Highest number is -', a)

elif(b>=a and b>=c and b>=d):
    print('Highest number is -', b)

elif(c>=b and c>=a and c>=d):
    print('Highest number is -', c)

elif(d>=c and d>=b and d>=a):
    print('Highest number is -', d)