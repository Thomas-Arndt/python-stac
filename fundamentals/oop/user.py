class user:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.acct_balance = 0

    def make_deposit(self, amount):
        self.acct_balance += amount
    
    def make_withdrawal(self, amount):
        self.acct_balance -= amount
    
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: " + str(self.acct_balance))
    
    def balance_transfer(self, other_user, amount):
        self.acct_balance -= amount
        other_user.acct_balance += amount
    

acct1 = user("Thomas Arndt", "arndtt42@gmail.com")
acct2 = user("Some Guy", "some_guy@gmail.com")
acct3 = user("Some Gal", "some_gal@gmail.com")

acct1.make_deposit(100)
acct1.make_deposit(150)
acct1.make_deposit(250)
acct1.make_withdrawal(75)
acct1.display_user_balance()

acct2.make_deposit(125)
acct2.make_deposit(75)
acct2.make_withdrawal(50)
acct2.make_withdrawal(100)
acct2.display_user_balance()

acct3.make_deposit(500)
acct3.make_withdrawal(100)
acct3.make_withdrawal(50)
acct3.make_withdrawal(150)
acct3.display_user_balance()

acct1.balance_transfer(acct3, 125)
print("Transfer 150 from Thomas to Some Gal")
acct1.display_user_balance()
acct3.display_user_balance()