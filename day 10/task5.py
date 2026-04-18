#1
class Students:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def display(self):
        print(self.name,self.mark)
s = [
    Students("A",90),
    Students("B",80),
    Students("C",40)
]

#2
for i in s:
    i.display()

#3
top = 0
for i in s:
    if i.mark>top:
        top = i.mark
print(top)