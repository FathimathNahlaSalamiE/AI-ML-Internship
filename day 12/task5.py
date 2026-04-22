#1
def count(n):
    for i in range(n):
        yield i
for num in count(5):
    print(num)

#2
def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
for num in even(11):
    print(num)

#3
def fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b
for num in fib(10):
    print(num)