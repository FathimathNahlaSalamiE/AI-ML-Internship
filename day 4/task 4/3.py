with open("data.txt","r") as file:
    lines = file.readline()
unique_lines = list(dict.fromkeys(lines))
with open("data.txt","w") as file:
    file.writelines(unique_lines)