#1
class BankAccount:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def check_balance(self):
        print(self.balance)
b = BankAccount("A")
b.deposit(500)
b.check_balance()
b.withdraw(700)
b.check_balance()

#2
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def discount(self,percent):
        d_amount = (self.price*percent)//100
        final_price = self.price - d_amount
        print("Name : ",self.name)
        print("Price : ",self.price)
        print("discount : ",percent),
        print("final_price : ",final_price)
p = Product("Carrot",80)
p.discount(50)