class BankAccount:
    account=[]
    def __init__(self, int_rate, balance):
        self.in_rate = int_rate
        self.balance = balance

    def deposit(self, amount): #deposit(self, amount) - increases the account balance by the given amount
        self.balance += amount
        return self

    def withdraw(self, amount): #withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print ("Insufficient funds: Charging a $5 fee and deduct $5")
            self.balance -= 5
        return self    
        
    def display_account_info(self): #display_account_info(self) - print to the console: eg. "Balance: $100"
        print ("Balance:$100")

    def yield_interest(self): #yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance  += (self.balance * self.in_rate)
            return self

#To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
#To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
yasmin = BankAccount(.1,5000)
liz = BankAccount (1.5,10000)

yasmin.deposit(100)
yasmin.deposit(100)
yasmin.deposit(100)
yasmin.withdraw(50)
yasmin.yield_interest()
yasmin.display_account_info()

liz.deposit(100)
liz.deposit(100)
liz.withdraw(20)
liz.withdraw(20)
liz.withdraw(40)
liz.withdraw(40)
liz.yield_interest()
liz.display_account_info()

""" Update the User class __init__ method

Update the User class make_deposit method

Update the User class make_withdrawal method

Update the User class display_user_balance method """

class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAccount(.02, 500)

    def make_deposit(self, amount):
        self.account += amount

    def make_withdrawal(self, amount):
        self.account -= amount    \

    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account}")

yasmin = User("yasmin")
liz = User("liz")



