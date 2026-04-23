#1
# nums = [1,2,3,4,3,2,1]

# s = []                                 for loop
# for n in nums:
#     s.append(n**2)
# print(s)

# s = [i**2 for i in nums]               list comprehension
# print(s)

# s = list(map(lambda i:i**2,nums))      map function
# print(s)

#2
# nums.sort()
# print(nums)

#3
def add(a,b):
    return a+b
print(add(2,10))
print(add(3,1))