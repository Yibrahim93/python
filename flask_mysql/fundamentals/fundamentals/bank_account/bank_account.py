class BankAccount:
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
Yasmin = BankAccount(.1,5000)
Adrian = BankAccount (1.5,10000)

Yasmin.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
Adrian.deposit(100).deposit(100).withdraw(20).withdraw(20).withdraw(40).withdraw(40).yield_interest().display_account_info()



