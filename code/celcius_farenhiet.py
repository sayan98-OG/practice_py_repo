class Temp_conv:
    def F_to_C(self,f):
        c = 5*(f-32)/9
        return c
    
    def C_to_F(self,c):
        f = ((c/5)*9)+32
        return f

    
i = int(input('''if you want to convert F to c press 1 
if you wanr to convert c to F press 2 : '''))    
    
x = Temp_conv()    
    
if i==2:
    cel = int(input('Enter celcius temparature :'))
    print (x.C_to_F(cel))
elif i==1:
    far = int(input('Enter farenheight temparature :'))
    print (x.F_to_C(far))    
else:
    print('Enter valid input : ')
