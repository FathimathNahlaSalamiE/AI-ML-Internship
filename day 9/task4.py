from task2 import students

#1
def avg(students):
    return sum(i["mark"] for i in students)//len(students)
print(avg(students))

#2
def topper(students):
    top = max(students,key=lambda i:i["mark"])
    return top["name"]
print(topper(students))

#3
def filt(students):
    return list(filter(lambda i:i["mark"]>75,students))
print(filt(students))