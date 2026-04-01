def factorial(a):
    if a <= 1:
        return 1
    else:
        return factorial(a)*factorial(a-1)
print(factorial(10))