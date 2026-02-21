# Mini Account system menu driven program
'''-------Menu----------------
1.create saving aaccount
2.create current account
3.deposit amount
4.withdrawal amount
5.check balance
6.Add Intrest
7.show account details
8.exit
enter your  choice(1to8)'''

#used oops concepts 
'''
1.class
2.object
3.inheritance
4.encapsulation
5.abstract
6.polymorphism'''

class BankAccount:

    def __init__(self,account_no,name,balance): #Encapsulation
        self._account_no=account_no             #data hiding/abstraction
        self._account_name=name
        self._balance=balance

    #deposite amount
    def DepoistAmount(self,amount):
        if amount>0:
            self._balance+=amount
            print(f'Rs.{amount} is deposited successfully to your account.your available balance is {self._balance}')
        else:
            print("Invalid Amount.... Pleasee Try Again")
    
    #withdrawal amount
    def withdrawal(self,amount):
        if amount>0 and amount<=self._balance:
            self._balance-=amount
            print(f'Rs.{amount} is withdrawal from your account.your available balance is {self._balance}')
        else:
            print("insufficient Balance.... Try again")
    
    #check balance
    def CheckBalance(self):
        print(f'Current Balance :-Rs.{self._balance}')
    

    ##account details
    def account_details(self):
        print('............Account Details...........')
        print(f'Account Number :- {self._account_no}')
        print(f'Account Holder Name :- {self._account_name}')
        print(f'Balance :-{self._balance}')
    

#herachical  inheritance 
class SavingAccount(BankAccount):
    
    def __init__(self,account_no,name,balance=0,rate_of_interest=0.03):
        super().__init__(account_no,name,balance)
        self._rate_of_interest=self._balance*rate_of_interest
    

    #add interest
    def add_interest(self):
        self.deposite(self._rate_of_interest)



#Inheritance :
class CurrentAccount(BankAccount):
    def __init__(self,account_no,name,balance=0,rate_of_interest=0.05):
        super().__init__(account_no,name,balance)
        self._rate_of_interest=self._balance*rate_of_interest
    

    #add interest
    def add_interest(self):
        self.deposite(self._rate_of_interest)




#Main funtion
if __name__ == "__main__":
    print("...Welcome To SBI Bank Account....../n")
    accounts={}
    ans='yes'
    while ans=="yes":
        print("------------Menu-----------------")
        print('1.Create Saving Account')
        print('2.Create Current Account')
        print('3.Deposit Amount')
        print('4.withdrawal Amount')
        print('5.Check Balance')
        print('6.Add Intrest')
        print('7.Show Account Details')
        print('8.Exit')

    #choose option from above option
        choice=int(input("Enter the Number between 1 to 8:"))

        #create Saving Account
        if choice==1:
            acct_no=int(input("Enter Your Account Number:"))
            if acct_no in accounts:
                print("Sorry.... Account Already Exits.....")
            else:
                acct_name=input("Enter Account Holder Name:")
                balance=eval(input("Enter Initial Balance: "))
                accounts[acct_no]=SavingAccount(acct_no,acct_name,balance)
                print(f'{acct_no} Saving Account Create successfully')

        #create Current account 
        elif choice==2:
            acct_no=int(input("Enter Your Account Number:"))
            if acct_no in accounts:
                print("Sorry.... Account Already Exits.........")
            else:
                acct_name=input("Enter Account Holder Name:")
                balance=eval(input("Enter Initial Balance"))
                accounts[acct_no]=SavingAccount(acct_no,acct_name,balance)
                print(f'{acct_no} Current Account Create successfully')


        #deposite amount in account
        elif choice==3:
            acct_no=int(input("Enter Your Account Number:"))
            if acct_no in accounts:
                amount=int(input("Enter Amount Which You Want TO Deposite:"))
                accounts[acct_no].DepoistAmount(amount)
            else:
                print("Account Not Found....")

        #withdrawal amount from account
        elif choice==4:
            acct_no=int(input("Enter Your Account Number:"))
            if acct_no in accounts:
                amount=int(input("Enter Amount Which You Want TO withdrawal:"))
                accounts[acct_no].withdrawal(amount)
            else:
                print("Account Not Found....")



        #check account balance.
        elif choice==5:
            acct_no=int(input("Enter Your Account Number:"))
            if acct_no in accounts:
                accounts[acct_no].CheckBalance()
            else:
                print("Account Not Found....")

        #add intrest to account
        elif choice==6:
            acct_no=int(input("Enter Your Account Number:"))
            if acct_no in accounts:
                accounts[acct_no].add_interest()
            else:
                print("Account Not Found....")


        #check account details
        elif choice==7:
            acct_no=int(input("Enter Your Account Number:"))
            if acct_no in accounts:
                accounts[acct_no].account_details()
            else:
                print("Account Not Found....")


        #exit for bank system
        elif choice==8:
            print("Thank You Showing Intrest In Our Bank System.....")


        else:
            print("Invalid Input... Please Give Valid Input......")
            




        ans=input("Do you Want To Continue..... Press 'yes' or 'no: ")


            
            

    
        
    