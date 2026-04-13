#1
students = [
    ["mark", 93],
    ["john", 90],
    ["mary", 91],
    ["anny", 69],
    ["mini", 70],
]

#2
print(students)

#3
marks = [i[1] for i in students]
print(sum(marks)//5)

#4
largest = 0
for i in students:
    if i[1]>largest:
        largest = i[1]
print(largest)

#5
print([i[0] for i in students if i[1]>75])