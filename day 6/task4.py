#1
student = [
    {"name": "mark", "mark": 90},
    {"name": "sony", "mark": 94},
    {"name": "riya", "mark": 87},
    {"name": "mary", "mark": 67},
    {"name": "elon", "mark": 34}
]

#2
topper = student[0]
for i in student:
    if i["mark"]>topper["mark"]:
        topper = i
print(topper)

#3
total = 0
for i in student:
    total += i["mark"]
print(total)

#4
passed = list(filter(lambda i: i["mark"] >= 50, student))
print(passed)