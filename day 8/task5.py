#1
arr1 = [1,2,3,4,5]
even = list(filter(lambda x:x%2==0,arr1))
print(even)

#2
arr2 = [
    {"student":"mark","mark":90},
    {"student":"riya","mark":40},
    {"student":"miya","mark":60},
    {"student":"lara","mark":70},
    {"student":"john","mark":49}
]
filt = list(filter(lambda x:x["mark"]>50,arr2))
print(filt)

#3
arr3 = ["hello","welcome","chairs","tables","tin"]
five = list(filter(lambda x:len(x)>5,arr3))
print(five)