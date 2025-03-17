def sum(n):
    if n==0:
        return 0
    else :
        return n+sum(n-1)


x = int(input('Enter the number: '))

print(sum(x))
