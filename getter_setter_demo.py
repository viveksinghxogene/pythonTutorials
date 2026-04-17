class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Amount can not be negative")
        self._balance = amount


acc = BankAccount("Vivek", 1000)
print(acc.balance)

acc.balance = 500
print(acc.balance)

acc.balance = -200