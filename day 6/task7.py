#1
l1 = [1,32,43,56,78,90,22]

l1.sort()
print(l1[1])

#2
l2 = [1,32,33,45,76,89,78]
l3 = list(set(l1 + l2))
print(l3)

#3
l4 = l1 + l2
freq = {}
for i in l4 :
    freq[i] = freq.get(i,0)+1
print(freq)
