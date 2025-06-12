class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit (self, amount):
        self.balance += amount
        print(f'Deposit {amount}. New balance: {self.balance}')
        
    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdraw {amount}. New balance: {self.balance}')
        else:
            print('Insufficient funds')
            
    def display_balance(self):
        print(f'Account {self.account_number} Balance: {self.balance}')
        
    
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        
        self.interest_rate = interest_rate
        
    def add_interest(self):
        interest = self.balance * self.interest_rate/100
        self.balance += interest
        print(f'Interest of {interest} was added . New balance is{self.balance}')
        

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f'Withdraw {amount}. New balance: {self.balance}')
        else:
            print('Exceeded the overdraft limit')
        
saving1 = SavingAccount('SA12003' , 100000, 5)
current1 = CurrentAccount('CA20041' , 20000, 10)

saving1.display_balance()
saving1.add_interest()
saving1.withdraw(20000)
print('LB ______________')

current1.display_balance()
current1.withdraw()
