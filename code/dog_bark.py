class Animal():
    def __init__(self, legs):
        self.legs = legs

class Pets(Animal):
    def __init__(self, legs, type):
        super().__init__(legs)
        self.type = type

class Dog(Pets):
    def __init__(self, legs, type,):
        super().__init__(legs,type)
        print(f'This is a dog, It has {self.legs} legs. It is a {self.type} animal.')
    @staticmethod
    def bark():
        print('Bhow Bhow!!')


apollo = Dog(4,'Domestic')
apollo.bark()