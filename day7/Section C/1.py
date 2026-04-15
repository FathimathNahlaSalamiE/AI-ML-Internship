d = []
total = 0
topper = 0

for i in range(5):

    # 1
    name = input("student name = ")
    mark = int(input("mark = "))

    # 2
    d.append({"name":name,"mark":mark})

    # 3
    total+=mark

    # 4
    if mark>0:
        topper = name

average = total//5

print(d)
print(average)
print(topper)