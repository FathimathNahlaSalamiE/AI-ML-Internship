a = [1,2,3,4]
#1
square = [i*i for i in a]
print(square)
#2
even = [i for i in a if i % 2 == 0]
print(even)
#3
b = ["abc","def","ghi"]
upper = [i.upper() for i in b]
print(upper)
#4
c = [1,2,3,4,5,10,20,30,400,50,90,78,89,78,56,45]
numbers = [i for i in c if i > 50]
print(numbers)