class BankAccount:
    def __init__ (self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def replenish(self, amount):
        self.balance += amount
    def withdrawal(self , amount):
        self.balance -= amount