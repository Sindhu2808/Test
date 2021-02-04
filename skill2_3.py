import csv
with open("attendance.csv",'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    next(reader)
    with open("finalattendance.csv",'w',newline='') as cs:
        writer = csv.writer(cs)
        writer.writerow(['ID', ' Name', ' Year', ' Section', ' CourseCode', ' Subject', ' NumberOfClassesConducted', ' NumberOfClassesPresent', ' NumberOfClassesAbsent','Percentage'])
        for row in reader:
            row.append((int(row[7]) / int(row[6])) * 100)
            writer.writerow(row)
