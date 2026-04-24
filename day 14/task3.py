import csv

#1,2      Create CSV file and Write student data
# with open("csv_file.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(['name','mark'])
#     writer.writerow(['john',80])

#3,4        Read CSV file and Print formatted output
with open("csv_file.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)