def calculate_average(student,marks):
    total = sum(marks)
    average = total/len(marks)
    return student,average
print(calculate_average("nahla",[20,20,20,10]))
print(calculate_average("john",[3,4,2,1]))

def power_list(nums, power):
    return [i**power for i in nums]
nums = [1,2,3,4]
print(power_list(nums,2))
print(power_list(nums,3))