import json

#1      Convert dictionary to JSON
python_data = {'name':'mary',"age":20}
json_data = json.dumps(python_data)
print("json => ",json_data)

#2      Convert JSON to dictionary
data = json.loads(json_data)
print("dictionary => ",data)

#3      Write JSON to file
with open("data.json","w") as file:
    json.dump(data,file)

#4      Read JSON from file
with open("data.json","r") as file:
    data = json.load(file)
    print(data)