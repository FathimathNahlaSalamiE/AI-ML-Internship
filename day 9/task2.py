#1
# with open("students.txt","w") as file:
#     for i in range(3):
#         name = input("enter student name : ")
#         mark = int(input("enter student mark : "))
#         file.write(name+","+str(mark)+"\n")

#2
students = []
with open("students.txt","r") as file:
    for line in file:
        name , mark = line.strip().split(",")
        students.append({"name":name,"mark":int(mark)})

if __name__ == "__main__":
    print(students)

    #3
    print([i["name"] for i in students])

    #4
    total = sum([i["mark"] for i in students])
    print(total//len(students))

    #5
    topper = (max(students,key=lambda i: i["mark"]))
    print(topper["name"])