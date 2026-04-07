file = open("data.txt","r")
lines = file.readlines()
print(len(lines))
file.close()