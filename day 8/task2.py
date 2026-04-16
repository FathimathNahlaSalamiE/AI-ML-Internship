#1
def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))

#2
def prime(num):
    for i in range(2,num):
        if num%i == 0:
            print("not a prime number")
            break
    else:
        print("it is a prime number")
prime(7)

#3
def rev(string):
    return string[::-1]
print(rev("hello"))

#4
def average(list,sum=0):
    for i in list:
        sum+=i
    avg = sum//len(list)
    return avg
print(average([1,2,3,4,5]))