try:
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))
    print(a/b)
except ValueError:
    print("input should be numbers")