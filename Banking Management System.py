class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance
    
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 1000:
            print("Limit exceeded for savings withdrawal")
        else:
            super().withdraw(amount)

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        self.__BankAccount__balance -= amount
        

acc1 = SavingsAccount("Dawood",5000)
acc1.withdraw(1500)
acc1.withdraw(500)

print(acc1.get_balance())
