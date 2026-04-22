#1
l1 = [1,2,3,4,5,1,2,3,4,5]
s1 = set(l1)
print(s1)

#2
s2 = {1,2,3,4,5,6,7,8,9}
common = s1 & s2
print(common)

#3
union = s1 | s2
difference = s2 - s1
print("union - ",union)
print("difference - ",difference)