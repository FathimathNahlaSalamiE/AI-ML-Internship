#1
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))

#2
def sum(num):
    if num == 1 :
        return 1
    else:
        return num+sum(num-1)
print(sum(10))

#3
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
num = 7
for i in range(num):
    print(fibonacci(i),end=" ")