class User:

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.accounts = []
        self.add_account()

    def make_deposit(self, amount, account=0):
        print("Depositing $"+str(amount)+" into account "+str(account)+"...")
        self.accounts[account].deposit(amount)
        return self
    
    def make_withdrawal(self, amount, account=0):
        print("Withdrawing $"+str(amount)+" from account "+str(account)+"...")
        self.accounts[account].withdraw(amount)
        return self

    def display_user_balance(self):
        for i in range(len(self.accounts)):
            self.accounts[i].display_account_info(i)
        return self
    
    def balance_transfer(self, other_user, amount, account=0):
        self.accounts[account].withdraw(amount)
        other_user.account.deposit(amount)
        return self
    
    def add_account(self):
        self.accounts.append(BankAccount(int_rate=0.02, balance=0))
        return self


class BankAccount:

    all_accounts = []

    def __init__(self, int_rate = 0, balance = 0):
        self.rate = int_rate
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

    def display_account_info(self, account):
        print("Account "+str(account)+" balance: $"+str(self.acct_balance))
        return self
    
    def yield_interest(self):
        self.acct_balance += self.acct_balance*self.rate
        return self

    @classmethod
    def display_all_info(cls):
        print("Information for all accounts:")
        for account in cls.all_accounts:
            account.display_account_info()

acct1 = User("Thomas Arndt", "arndtt42@gmail.com")
acct1.add_account().make_deposit(100).make_deposit(200, 1).make_withdrawal(200,0).make_withdrawal(50, 0).display_user_balance()