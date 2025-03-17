
def star(n):
    if n==0:
        print('')
    else :    
        print(n*'*')
        star(n-1)

no = int(input('Enter the number of star: '))

star(no)
