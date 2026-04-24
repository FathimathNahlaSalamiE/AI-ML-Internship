import csv,json

python_dictionary = {}
#1
with open("csv_file.csv","r") as file:
    reader = csv.DictReader(file)
#2
    for row in reader:
        python_dictionary[row["name"]] = int(row["mark"])
    print(python_dictionary)
    # reader = csv.reader(file)
    # header = next(reader)
    # for row in reader:
    #     name = row[0]
    #     mark = int(row[1])
    #     python_dictionary[name] = mark
    # print(python_dictionary)

#3 save in a json file
with open("json_data.json","w") as file:
    json.dump(python_dictionary,file)
# convert to json
# json_data = json.dumps(python_dictionary)
# print(json_data)