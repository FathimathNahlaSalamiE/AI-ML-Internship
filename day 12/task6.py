# names = ["AI", "ML"]
# for i, name in enumerate(names):
#     print(i, name)

# names = ["A", "B"]
# marks = [80, 90]
# combined = list(zip(names, marks))
# print(combined)

#1
l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
combine = list(zip(l1,l2))
print(combine)

#2
for i,j in enumerate(l2):
    print(i,j)

#3
d = dict(zip(l1,l2))
print(d)