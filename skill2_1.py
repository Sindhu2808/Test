import csv
with open("attendance.csv",'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)







