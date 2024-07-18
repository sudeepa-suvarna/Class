class Student:
    idGenerator = 101
    def __init__(self,name = '',marks = 0):
        self.id = Student.idGenerator
        self.name = name
        self.marks = marks
        self.idGenerator += 1
        Student.idGenerator += 1
    # def __str__(self):
    #     stdentStr = 'ID=' + str(self.id) + 'name:' + self.name + 'marks:' + str(self.marks)
    #     return stdentStr
#s1 = Student("Sudeepa",75)
#print("Students details are",s1 )

class StudentOperstions:
    Stduents = []
    def createStudent():
        stName = input("Enter the student name")
        stMarks = int(input("Enter the marks"))
        s1 = Student(stName,stMarks)
        StudentOperstions.Stduents.append(s1)

    def listStudent():
        if len(StudentOperstions.Stduents)==0:
            print("No element to show")
        else:
            print('{:<5} {:<15} {:<5}'.format("ID","NAME","MARKS"))
            print('-'*25)
            for student in StudentOperstions.Stduents:
                print("{:<5} {:<15} {:<5}".format(student.id,student.name,student.marks))
    def updateStudent():
        if len(StudentOperstions.Stduents)==0:
            print("No element to show")
        else:
            stId = int(input("Enter the student id"))
            isStudent = True
            for i in range(len(StudentOperstions.Stduents)):
                if StudentOperstions.Stduents[i].id == stId:
                    isStudent = False
                    stMarks = int(input("Enter the marks"))
                    StudentOperstions.Stduents[i].marks=stMarks
            if isStudent:
                print("Student not found")
    def deleteStudent():
        if len(StudentOperstions.Stduents)==0:
            print("No element to show")
        else:
            stId = int(input("Enter the student id"))
            isStudent = True
            for i in range(len(StudentOperstions.Stduents)):
                if StudentOperstions.Stduents[i].id == stId:
                    isStudent = False
                    del StudentOperstions.Stduents[i]
            if isStudent:
                print("Student not found")
    def searchStudent():
        if len(StudentOperstions.Stduents)==0:
            print("No element to show")
        else:
            stId = int(input("Enter the student id"))
            isStudent = True
            for i in range(len(StudentOperstions.Stduents)):
                if StudentOperstions.Stduents[i].id == stId:
                    isStudent = False
                    print('{:<5} {:<15} {:<5}'.format("ID","NAME","MARKS"))
                    print('-'*25)
                    print("{:<5} {:<15} {:<5}".format(StudentOperstions.Stduents[i].id,StudentOperstions.Stduents[i].name,StudentOperstions.Stduents[i].marks))
            if isStudent:
                print("Student not found")







    def sortStudents():
        print("Sorted student list")
        for i in range(0,len(StudentOperstions.Stduents)):
            sorted = True
            for j in range(0,len(StudentOperstions.Stduents)- i -1):
                if StudentOperstions.Stduents[j].marks > StudentOperstions.Stduents[j+1].marks:
                    sorted = False
                    StudentOperstions.Stduents[j],StudentOperstions.Stduents[j+1] = StudentOperstions.Stduents[j+1] , StudentOperstions.Stduents[j]
            if sorted:
                break
        print('{:<5} {:<15} {:<5}'.format("ID","NAME","MARKS"))
        print('-'*25)
        for student in StudentOperstions.Stduents:
            print("{:<5} {:<15} {:<5}".format(student.id,student.name,student.marks))    
def exitProgram():
    exit("Enf of program")
def invalidInput():
    print("invalid input entered")


menu = {
    1:StudentOperstions.createStudent,
    2:StudentOperstions.listStudent,
    3:StudentOperstions.sortStudents,
    4:StudentOperstions.updateStudent,
    5:StudentOperstions.deleteStudent,
    6:StudentOperstions.searchStudent,
    7:exitProgram
    
}

while True:
    print("1.Create Student\n2.List all\n3.Sort Record\n4.Update student\n5.Delete Student\n6.Search Student\n7.Exit\nYour choice")
    choice = int(input())
    menu.get(choice, invalidInput)()




































'''def bubble_sort(array,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
inputSize = int(input("Enter the size of the array:"))
print(f"Enter {inputSize} elements of array")
array = []
for i in range(inputSize):
    elements=int(input())
    array.append(elements)
print(f"User given elements aare{array}")
bubble_sort(array,inputSize)
print(f"The sorted element are \n {array}")'''
