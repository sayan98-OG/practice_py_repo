
def avg():
     a = int(input('Enter a number: '))
     b = int(input('Enter a number: '))
     c = int(input('Enter a number: '))

     average = (a+b+c)/3
     print(average)

avg()     

#functions with arguments

def greetings(name):
     print(f'Hey {name}, have a nice day!!')
     return "Hola"


a = greetings('Sayan')     
print(a)