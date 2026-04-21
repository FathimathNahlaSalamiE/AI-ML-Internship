class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print("Animal make sound")
class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")

obj = Dog("dog")
obj.sound()