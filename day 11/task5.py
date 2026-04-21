class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def __init__(self,salary):
        super().__init__("abbc")
        self.salary = salary
    def display(self):
        print(self.name,self.salary)
obj = Employee(80)
obj.display()