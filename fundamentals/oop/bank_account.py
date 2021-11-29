class BankAccount:

    all_accounts = []

    def __init__(self, init_rate = 0, balance = 0):
        self.rate = init_rate
        self.acct_balance = balance
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.acct_balance += amount
        return self
    
    def withdraw(self, amount):
        if self.acct_balance < amount:
            print("You do not have enough funds for this withdrawal")
        else:
            self.acct_balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $"+str(self.acct_balance))
        return self
    
    def yield_interest(self):
        self.acct_balance += self.acct_balance*self.rate
        return self

    @classmethod
    def display_all_info(cls):
        print("Information for all accounts:")
        for account in cls.all_accounts:
            account.display_account_info()
    

acct1 = BankAccount(0.1, 100)
acct2 = BankAccount(0.25, 100)

acct1.deposit(100).deposit(200).deposit(50).withdraw(150).yield_interest().display_account_info()
acct2.deposit(250).deposit(50).withdraw(25).withdraw(225).withdraw(25).withdraw(50).yield_interest().display_account_info()

BankAccount.display_all_info()