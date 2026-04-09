#this program is to demonstrate the usage of encapsulation

class Student:
    major = "Cloud Computing and Devops"

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name


s1 = Student(1, "Vivek")
s2 = Student(2, "Deepak")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)