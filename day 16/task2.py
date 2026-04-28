#1
list_a = [
    {"name": "miya","mark":90 },
    {"name": "niya", "mark": 80},
    {"name": "riya", "mark": 50},
    {"name": "diya", "mark": None},
    {"name": "liya", "mark": 30}
]
result_1 = [i for i in list_a if i["mark"] is not None]
print(result_1)

#2
list_b = [
    {"name": "miya","mark":90 },
    {"name": "niya", "mark": 80},
    {"name": "riya", "mark": 50},
    {"name": "diya", "mark": -20},
    {"name": "liya", "mark": 30}
]
result_2 = [i for i in list_b if i["mark"] >= 0]
print(result_2)

#3
list_c = [
    {"name": "miya","mark":90 },
    {"name": "niya", "mark": 80},
    {"name": "riya", "mark": 50},
    {"name": "diya", "mark": "abd"},
    {"name": "liya", "mark": 30}
]
result_3 = [i  for i in list_c if isinstance(i["mark"], int)]
print(result_3)