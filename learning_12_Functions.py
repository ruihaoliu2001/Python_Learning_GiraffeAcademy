
def say_hi(name, age): #创建一个函数，下方所有缩进的内容都会被视作函数的部分；括号内可以添加参数
    print("Hello " + name + "!\n" + "You are" , age , "!")

print("Top")
say_hi(input("Enter a name: "),input("Enter a number: ")) #调用函数。python中变量的类型是根据我们输入的类型自动赋予的，见variable一节
# 会依次显示input
print("Bottom") #这三行依次进行，当到say_hi()时跳到该函数定义的部分，执行完毕后跳回