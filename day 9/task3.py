from task2 import students

#1
print(list(filter(lambda i:i["mark"]>75,students)))

#2
print(len(students))

#3
lowest = min(students,key=lambda i:i["mark"])
print(lowest["mark"])

#4
sorted_students = sorted(students,key=lambda i:i["mark"],reverse=True)
for i in sorted_students:
    print(i["name"],">",end="")