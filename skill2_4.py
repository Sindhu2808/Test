import csv
with open("finalattendance.csv",'r') as csvfile:
    print('Student Record by ID and Name')
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if float(row[9])<=60:
            print(row)
