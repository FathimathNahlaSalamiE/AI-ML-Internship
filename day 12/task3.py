#1
d1 = {i:i*i for i in range(1,11)}
print(d1)

#2
d2 = {i:i**2 for i in d1 if i % 2 == 0}
print(d2)

#3
l = ["hello","world","welcome"]
d3 = {i:len(i) for i in l}
print(d3)