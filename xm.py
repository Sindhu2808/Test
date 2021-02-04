
class Students:
     def __init__(self, id, fname, lname, course, year, gpa, uname, mobile):
            self.id = id
            self.fname = fname
            self.lname = lname
            self.course = course
            self.year = year
            self.gpa = gpa
            self.uname = uname
            self.mobile = mobile

while (True):
    id = int(input("Enter ur ID: "))
    fname = input("Enter ur First name: ")
    lname = input("Enter ur Last name: ")
    course = input("Enter ur Course: ")
    year = int(input("Enter ur Acedemic Year: "))
    gpa = float(input("Enter ur GPA: "))
    uname = input("Enter ur University Name: ")
    mobile = int(input("Enter ur Mobile Num: "))

def getMail():
    email = fname + lname + "@gmail.com"
    return email
x = Students(id, fname, lname, course, year, gpa, uname, mobile)
print("====================================")
print(
f"ID : {x.id}\nFirstName : {x.fname}\nLastName :{x.lname}\nCourse:{x.course}\nAcademic Year :{x.year}\nGPA :{x.gpa}\nUniversity:{x.uname}\nMobileNo :{x.mobile}\nMailID :{getMail()}")
print("====================================")
print("Do you want to add one more???\nChoose:- y/n")
opt = input();
if (opt == "y"):
    pass

