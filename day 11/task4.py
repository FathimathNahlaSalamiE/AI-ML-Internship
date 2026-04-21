class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        self.__balance -= amount
    def check_balance(self):
        return self.__balance

obj = BankAccount("nahla",90)
obj.deposit(100)
obj.withdraw(90)
print(obj.check_balance())