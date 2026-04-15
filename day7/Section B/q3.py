a = "hello WORLD"
count = 0
for i in a.lower():
    if i in "aeiou":
        count+=1
print(count)