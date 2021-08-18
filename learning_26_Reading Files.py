

employee_file = open("Reading Files.txt", "r")
# r：只读；w：只写；a：添加；r+：读和写……
# 注意将读取的文件赋给一个变量很重要，便于之后操作

print(employee_file.readable())  # 查看是否可读，返回True or False（若上方r换成w，则此处输出False）

print(employee_file.readlines()) #可以把每一行作为list的一个元素构成list
employee_file.close()

# 由于文件是指针操作，如果这里不close，对该文件的指针会在末尾，所以继续运行只能输出空行
# 因此要时刻记住关闭文件！！！
print("/////")

employee_file = open("Reading Files.txt", "r") #再次打开文件
print(employee_file.read())
employee_file.close()

print("/////")

employee_file = open("Reading Files.txt", "r") #再次打开文件
if employee_file.readable():
    print(employee_file.readline()) #一行一行的输出，写几个该命令，依次输出几行
    print(employee_file.readline())
    print(employee_file.readline())#此时不输出是因为之前read过了，指针已经指向了文件末尾，相当于读出了最后几个空行
else:
    print("File cannot be read!")
employee_file.close() #结束后总是需要关闭文件

print("/////")

employee_file = open("Reading Files.txt", "r") #再次打开文件
print(employee_file.readlines()[1]) #xxx.readlines()实际构成了一个list
employee_file.close()

print("/////")

employee_file = open("Reading Files.txt", "r") #再次打开文件
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

print("/////")

employee_file = open("Reading Files_w.txt", "w") #再次打开文件，以w的方式
employee_file.close()
# 会发现这一操作执行后，文件变成了空的

print("/////")

employee_file = open("/Users/caoyang98/Desktop/Python/pycharm_learn/tesy.txt", "r") #再次打开文件，以w的方式，这次尝试绝对地址
print(employee_file.read())
employee_file.close()
