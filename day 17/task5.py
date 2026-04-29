import matplotlib.pyplot as plt

x = [1,10,3]
y = [2,4,6]

#1
# plt.plot(x,y)
# plt.show()

#2
# plt.bar(x,y)
# plt.show()

#3
subject = ["physics","chemistry","maths","english","malayalam"]
mark = [89,90,79,100,100]
plt.bar(subject,mark)
plt.show()