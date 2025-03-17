class complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, num2):
        return (self.r+num2.r , self.i+num2.r)    
    
    def __str__(self):
        return f"{self.r} {self.i}i"
    
    a= complex(1,2)
    b= complex(6,3)

    print(a+b)