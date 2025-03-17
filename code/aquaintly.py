class social():
    db = {}
    def createdtabase(self,e:list):
        status = e[0]
        u1 =  e[1]
        u2 = e[2]
        
        if status == 'CONNECT':
            try:
                self.db[u1] += 1
            except:
                self.db[u1] = 1
            try:
                self.db[u2] += 1
            except:
                self.db[u2] = 1    
        elif status == 'DISCONNECT':
            self.db[u1]-=1
            self.db[u2]-=1
               
    def listing(self, log :list, con :int):
        for i in log:
            self.createdtabase(i)
        list1 = [key for key,value in self.db.items() if value < con]
        list2 = [key for key,value in self.db.items() if value >= con]
        finallist = [list1,list2]

        return finallist

events = [
   ["CONNECT","Alice","Bob"],
   ["DISCONNECT","Bob","Alice"],
   ["CONNECT","Alice","Charlie"],
   ["CONNECT","Dennis","Bob"],
   ["CONNECT","Pam","Dennis"],
   ["DISCONNECT","Pam","Dennis"],
   ["CONNECT","Pam","Dennis"],
   ["CONNECT","Edward","Bob"],
   ["CONNECT","Dennis","Charlie"],
   ["CONNECT","Alice","Nicole"],
   ["CONNECT","Pam","Edward"],
   ["DISCONNECT","Dennis","Charlie"],
   ["CONNECT","Dennis","Edward"],
   ["CONNECT","Charlie","Bob"]
]


a=social()
print(a.listing(events, 2))
 