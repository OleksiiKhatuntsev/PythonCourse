class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        if money >= 0:
            print(f"Previous balance: {self.balance}, new balance: {self.balance + money}")
            self.balance += money
        else:
            print(f"Try to withdrawal with {-money}")
            return self.withdrawal(-money)

    def withdrawal(self, money):
        if money >= 0:
            if(self.balance - money) < 0:
                print("Cannot do this, balance will be {}".format(self.balance - money))
            else:
                print(f"Previous balance: {self.balance}, new balance: {self.balance - money}")
                self.balance -= money
        else:
            print(f"Making a deposit with {-money}")
            return self.deposit(-money)

    def __str__(self):
        return (f"Owner:   {self.owner}\nbalance: {self.balance}$")

account = Account("Alex", 100)

print(account)
print(account.balance)
print(account.owner)
account.deposit(200)
account.deposit(-200)
account.withdrawal(100)
account.withdrawal(-100)