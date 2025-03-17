class Password_validation:
    
    def __init__(self, pcode):
        self.rule = []
        self.pcode = pcode
        self.pcodel = pcode.lower()
 
    def rule1(self):
        if len(self.pcode)<=15:
            self.rule.append(1)
    def rule2(self):        
        if "password" in self.pcodel:
            self.rule.append(2) 
    def rule3(self): 
        flag = 0        
        for i in self.pcode:
            if self.pcode.count(i)>4:
                flag +=1           
        if flag>0:
            self.rule.append(3)
    def rule4_1(self): 
        flag = 10        
        for i in self.pcode:
            if i.islower():
                flag +=1           
        if flag == 10 and self.rule.count(4)!=1:
            self.rule.append(4) 
    def rule4_2(self): 
        flag = 10        
        for i in self.pcode:
            if i.isupper():
                flag +=1           
        if flag == 10 and self.rule.count(4)!=1:
            self.rule.append(4)                
    def rule5(self): 
        flag = 0        
        for i in self.pcode:
            if i=='*' or i == '#' or i == '@':
                flag += 1       
        if flag == 0:
            self.rule.append(5) 
        
    def validate(self):
        self.rule1()
        self.rule2() 
        self.rule3() 
        self.rule4_1()
        self.rule4_2() 
        self.rule5()
        return self.rule
        self.rule = []
        
        
passcodes = ["Strongpwd9999#ac","Aess10#","Password@","#PassWord011111112222223x","PASSWORDz#1111111","aaaapassword$$","LESS10#","SsSSSt#passWord","SsSSSt#passWordpassword","aZ*"]  

for i in passcodes:
    pc = Password_validation(i)
    print(pc.validate())
    # Password_validation.rule = []

# pc = Password_validation('aaaapassword$$')
# print(pc.validate())