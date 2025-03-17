num = int(input('Enter a number: '))
flag = 0
if num==1 or num==2:
    pass
else :
    for i in range (2,num):
        if (num%i==0):
            flag = flag+1

if (flag==0):
    print('Number is prime')
else :
    print('Number is not prime')
