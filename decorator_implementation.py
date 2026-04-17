# i have implemented the getter setter through decorators in this application
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def validate_amount(func):
        def wrapper(self, amount):
            if amount < 0:
                raise ValueError("Amount can not be negative")
            return func(self, amount)
        return wrapper

    @property
    def balance(self):
        return self._balance

    @balance.setter
    @validate_amount
    def balance(self, amount):
        self._balance = amount


acc = BankAccount("Vivek", 1000)
print(acc.balance)

acc.balance = 500
print(acc.balance)

acc.balance = -200