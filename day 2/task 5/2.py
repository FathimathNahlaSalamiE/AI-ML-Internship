def prime(a):
    for i in range(2,a):
        if a%i==0:
            break
    else:
        return True
print(prime(9))