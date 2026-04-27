#1
marks = [90,80,50,40,None,-10,-1]

# 2
remove_none = [i for i in marks if i is not None]
print(remove_none)

#3
remove_negative = [i for i in remove_none if i>0]
print(remove_negative)

#4
data = [10, None, -5, "abc", 25, -2, 40]
cleaned = [x for x in data if isinstance(x, (int, float)) and x >= 0]
print(cleaned)