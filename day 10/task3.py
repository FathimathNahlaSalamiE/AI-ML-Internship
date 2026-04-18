#1
class Student:
    #2
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
#3
s = Student("john",90)
print(s.name,s.mark)