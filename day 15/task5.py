from itertools import count

marks = [90,80,50,40]

#1
print([i/100*100 for i in marks])

#2
print([i*2 for i in marks])

#3
min_val = min(marks)
max_val = max(marks)
normalized = [(x - min_val) / (max_val - min_val)for x in marks]
print(normalized)