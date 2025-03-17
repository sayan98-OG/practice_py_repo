
n = int(input('Enter a number: '))
i=1
while (i<n+1):
    print(i*'*')
    i += 1

for l in range (n+1):
    print((n-l)*' ',(2*l-1)*'*')

for m in range (n+1):
    if m==0:
        continue
    print((m)*' ',((2*n-1)-2*m)*'*')

for g in range (1,n+1):
    if g==1 or g==n:
        print('*'*n)
    else :
        print('*',(n-2)*' ','*')

