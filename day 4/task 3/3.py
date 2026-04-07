try:
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero")
else:
    print("b is not zero")
finally:
    print("code executed")