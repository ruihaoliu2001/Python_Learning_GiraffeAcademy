
"""
employee_file = open("Reading Files_w.txt", "w")
employee_file.write("Xavi -- Football Player")
employee_file.close()
# 仅仅w会覆盖原先的文件内容，指针指向文件头部。应该用a来在文件的末尾进行添加
"""

employee_file = open("Reading Files_w.txt", "a")
employee_file.write("23Xavi -- Football Player")
employee_file.close()
#注意，如果多次运行该段程序，会出现添加同一内容在同一行多次的情况。由于a始终认为添加在了文件的末尾，指针默认指向这里，所以若文件本身没有新的一行，就会直接添加在末尾。

#因此可以考虑添加\n，以确保在新行添加文字：
employee_file = open("Reading Files_w.txt", "a")
employee_file.write("\nXavi -- Football Player")
employee_file.close()

employee_file = open("Reading Files_new.txt", "w")
employee_file.write("This file is written manually using python program \" learning_27\"")
employee_file.close()

