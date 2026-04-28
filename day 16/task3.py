#1
list_a = [
    {"name": "miya","mark":90 },
    {"name": "niya", "mark": 80},
    {"name": "riya", "mark": 50},
    {"name": "diya", "mark": 60},
    {"name": "liya", "mark": 30}
]
result_a = [{**i,"status": "pass" if i["mark"] >= 0 else "fail"}for i in list_a]
print(result_a)


#2
list_b = [
    {"name": "miya","mark":90 },
    {"name": "niya", "mark": 80},
    {"name": "riya", "mark": 50},
    {"name": "diya", "mark": 60},
    {"name": "liya", "mark": 30}
]
result_b = [{**i,"mark":i["mark"]/100*100} for i in list_b]
print(result_b)

#3
list_c = [
    {"name": "miya","mark":90 },
    {"name": "niya", "mark": 80},
    {"name": "riya", "mark": 50},
    {"name": "diya", "mark": 60},
    {"name": "liya", "mark": 30}
]
result_c = [{**i,"percentage":i["mark"]/100*100} for i in list_c]
print(result_c)