# import csv
import pandas as pd
# with open("students.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(['name','marks','city'])
#     writer.writerow(['john',80,'kochi'])
#     writer.writerow(['Anu',80,'calicut'])
#     writer.writerow(['arjun',80,'kollam'])

df = pd.read_csv("students.csv")

print(df)
