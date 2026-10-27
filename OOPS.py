class Student:
    college_name = "ABC college"
    def __init__(self, name, marks ):
        self.name = name
        self.marks = marks
        print("adding new student to the Database")


s1 = Student("karan", 98)
print(s1.name, s1.marks)

s2 = Student("Yajat", 56)
print(s2.name, s2.marks)

print(Student.college_name)