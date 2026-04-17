from itertools import count

from task2 import students

#1
sorted_students = sorted(students,key=lambda i:i["mark"],reverse=True)
print([sorted_students[1]["name"]])

#2
passed = len(list(filter(lambda i:i["mark"]>70,students)))
failed = len(list(filter(lambda i:i["mark"]<70,students)))
print(passed,failed)

#3
student_dictionary = {}
with open("students.txt","r") as file:
    for line in file:
        name, mark = line.strip().split(",")
        student_dictionary[name] = int(mark)
print(student_dictionary)