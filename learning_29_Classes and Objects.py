
import learning_29_Student
student1 = learning_29_Student.Student("Raymond", "Physics", 3.91, False)
student2 = learning_29_Student.Student("Denny", "Business", 3.03, True)

# 之前大写的Student是一个class，结构体类型；这里的student_1和student_2是实际的对象（object）

"""
另一种写法：（和第28节的两种写法类似）
from learning_29_Student import Student
student1 = Student("Raymond", "Physics", 3.91, False)
"""

print(student1.major, "\n", student2.gpa, sep="")



# 不是student1.major()，若这么写，会报错TypeError: 'str' object is not callable，由于major不是函数，不能被调用

