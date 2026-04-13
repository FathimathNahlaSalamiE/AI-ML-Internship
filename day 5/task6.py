#1
a = [12,45,3,87,90,56,74]
a.sort(reverse=True)
print(a[1])

#2
b = "hello world"
b = "".join(b.split())
frequency = {}
for i in b:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)

#3
c = [12,45,3,87,90,56,74,1,2,3,12,45,74,56,90,1,3]
print(list(set(c)))