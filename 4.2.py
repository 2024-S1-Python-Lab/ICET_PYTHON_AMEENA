class Bank:
    def __init__(self,accno,name,acctype,balence=0):
        self.accno=accno
        self.name=name
        self.acctype=acctype
        self.bal=balence
    def deposit(self,amount):
        if amount>0:
            self.bal+=amount
            print(f'Deposit successful!, New balance:{self.bal}')
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self,amount):
        if amount>0:
            if amount<=self.bal:
                self.bal-=amount
                print(f"Withdrawal successful!. New balence:{self.bal}")
            else:
                print("Invalid withdrawal amount.Please enter a positive value.")
    def display(self):
        print(f'\n Account Number:{self.accno} \n Account Holder Name: {self.name} \n Accont Type:{self.acctype} \n Balance:{self.bal}')
        print('\n ****Menu****')
        print('1.Deposit \n 2.Withdraw \n 3.Display \n 4.Exit')

b1=Bank(1000554,'Ayisha',"Saving",0)
b1.display()
while True:
    choice=int(input('Enter your choice(1-4):'))
    if choice==1:
        d=int(input('Enter amount to be deposited:'))
        b1.deposit(d)
    if choice==2:
        w=int(input('Enter amount to be deposited:'))
        b1.withdraw(w)
    if choice==3:
        b1.display()
    if choice==4:
        print("Exiting... Thank You!")
        break
    else:
        print('Enter a valid choice')
        