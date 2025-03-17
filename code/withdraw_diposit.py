class Bank_account:
    
    def __init__(self, accountnumber: str):
        self.__accountnumber = accountnumber
        self.__amount = 0
        print('Welcome!!!')

    def diposit(self, dipositamount):
        if dipositamount>0:
            print(f'{dipositamount} is diposited')
            self.__amount += dipositamount
        else:
            print('Enter a valid amount')  

    def withdraw(self, withdrawamount):
        if withdrawamount>0:
            print(f'{withdrawamount} is withdrawn')
            self.__amount -= withdrawamount
        else:
            print('Enter a valid amount')            

    def display(self):
        print(f'Account number : {self.__accountnumber}')
        print(f'Amount : {self.__amount}')    

        
sayan = Bank_account('7003961622')

sayan.display()
i = int(input('\nFor diposit press 1 and to withdraw press 2 : '))

if i == 1:
    d = int(input('\nEnter diposit ammount : '))
    sayan.diposit(d)
elif i == 2:
    w = int(input('\nEnter withdraw ammount : '))
    sayan.withdraw(w)    
else :
    print('\nInvalid input')
sayan.display()
