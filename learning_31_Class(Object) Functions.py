
from learning_29_Student import Student

student1 = Student("Raymond", "Physics", 3.91, False)
student2 = Student("Denny", "Business", 3.03, True)

students = [student1, student2]

def is_honor(student):
    if student.on_honor():
        print(student.name + " is a good student!")
    else:
        print(student.name + " is not a good student!")
# 检测是否gpa大于3.5程序

for student in students:
    is_honor(student)