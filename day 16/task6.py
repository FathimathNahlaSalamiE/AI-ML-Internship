list_a = [
    {"name": "miya","mark":90 },
    {"name": "niya", "mark": 80},
    {"name": "riya", "mark": 50},
    {"name": "diya", "mark": 60},
    {"name": "liya", "mark": 30}
]

marks = [i["mark"] for i in list_a]

#1
avg = sum(marks)/len(marks)
print(avg)

#2
high = max(marks)
print(high)

#3
low = min(marks)
print(low)