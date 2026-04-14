a = [1,32,45,76,89,90,87,65,44,1,2,34,56,87,90]

#1
print(max(a))
print(min(a))

#2
a = list(set(a))
a.sort()
print(a[-2])

#3
print(list(set(a)))

#4
even = 0
odd = 0
for i in a:
    if i%2 == 0:
        even+=1
    else:
        odd += 1
print("even = ", even, "\nodd = ",odd)