file = open("data.txt","r")
text = file.read()
vowels = "aeiouAEIOU"
count = 0
for i in text:
    if i in vowels:
        count+=1
print(count)
file.close()