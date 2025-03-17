class Two_d():
    def __init__(self,i,j):
        self.i = i
        self.j = j
class Three_d(Two_d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

o = Three_d(12,45,69)
print (o.i,o.j,o.k)
