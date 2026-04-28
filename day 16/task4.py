#1
list_a = [
    {"name": "miya","mark":90 },
    {"name": "niya", "mark": 80},
    {"name": "riya", "mark": 50},
    {"name": "diya", "mark": 60},
    {"name": "liya", "mark": 30}
]
result_a = sorted(list_a, key= lambda i:i["mark"] , reverse=True)
# data handling
top_3 = sorted(list_a, key=lambda i: i.get("mark", 0), reverse=True)[:3]
print(result_a)

#2
print(result_a[:3])