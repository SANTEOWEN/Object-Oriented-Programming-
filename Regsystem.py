class Student:
    def __init__(self, Name, Course, Year, Section):
        self.name = Name
        self.course = Course
        self.year = Year
        self.section = Section

    def introduce(self):
        print("Name    : " + self.name)
        print("Course  : " + self.course)
        print("Year    : " + self.year)
        print("Section : " + self.section)

#we declare this variable so we can store all of the input comming from users this represents the storage of the inputs
listofstudent = []

while True:
    #we need to get all of the input from the users using while loop we can endlessly ask them some cridentials that we need
    print()
    name = input("Name         :")
    course = input("Course     :")
    year = input("Year         :")
    section = input("Section   :")
    
    #every inputs comming from user will be gather here and will be directed on the variable (listofstudents) 
    s = Student(name, course, year, section)
    listofstudent.append(s)
    print()
    #we also created another input inorder for the user to choose if they want to create another user or not we use for loop to set the make it posible
    choice = input("Create Another Student? [Y/any char] : ")

    if choice == 'Y' or choice == 'y':
        pass
    else: 
         break
#we also use for loop to use the function(introduce) that we created so we can simple view our input by declaring the (list of student) from the previous input with student number 
s_num = 1 
for Student in listofstudent:
    print()
    print("Student#" + str(s_num))
    Student.introduce()
    s_num = s_num + 1 