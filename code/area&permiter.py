class Rectangle:
    def __init__(self, height, width):
        if height>0 and width>0:
            self.__height= height
            self.__width= width
        else :
            print('Enter valid measures!')    
    
    def area(self):
        self.__area= self.__height*self.__width 
        print(f'Area : {self.__area}') 

    def perimiter(self):
        self.__perimiter= 2*(self.__height+self.__width)
        print(f'Perimiter : {self.__perimiter}')



try:
    l = int(input('Enter a length : '))
except:
    print('Enter a valid length')
try:
    w = int(input('Enter a width : '))
except:
    print('Enter a valid width')
plot1 = Rectangle(l,w)
try:
    plot1.area()
except:
    print("Length or Width can't be zero or negative " )    

try:
    plot1.perimiter()
except:
    print("Length or Width can't be zero or negative " )  
        