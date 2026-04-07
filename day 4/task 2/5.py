file = open("data.txt","r")
text = file.read()
words = text.split()
print(len(words))