# 使用class来自己定义一种数据类型

class Student: #一般class类型用大写首字母
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name  #意义：self.name是对象（object）的实际name，右边的name是我们给传递的参数
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        # 以上的各个名称要对应一致，这个__init__函数是规定该类型基本特征的本征函数

    def on_honor(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False   # 结构体class的函数






# 类似C语言中的结构体