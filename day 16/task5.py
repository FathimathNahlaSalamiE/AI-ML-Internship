#1
list_a = [
    {"name": "miya","mark":90 },
    {"name": "niya", "mark": 80},
    {"name": "riya", "mark": 50},
    {"name": "diya", "mark": 60},
    {"name": "liya", "mark": 30}
]
result_a ={"pass":[],"fail":[]}
for i in list_a:
    if i["mark"] >= 50:
        result_a["pass"].append(i)
    else:
        result_a["fail"].append(i)
print(result_a)

#2
print(len(result_a["pass"]))
print(len(result_a["fail"]))