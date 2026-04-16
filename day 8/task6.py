#1
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return (num%10)+sum_of_digits(num//10)
print(sum_of_digits(986))

#2
def flatten(arr):
    result = []
    for i in arr:
        if isinstance(i,list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
print(flatten([1,2,[3,[4,5]],[6,7]]))

#3
def occurrence(word):
    d = {}
    for i in word:
        d[i]=d.get(i,0)+1
    return d
print(occurrence("malayalam"))