import csv
with open("attendance.csv",'r') as csvfile:
    print('Student Record by ID and Name')
    reader = csv.reader(csvfile)
    next(reader)
    next(reader)
    id=int(input('Enter your ID'))
    name=input('Enter Student Name')
    for row in reader:
        if id==int(row[0]) and name==row[1]:
            print(row)