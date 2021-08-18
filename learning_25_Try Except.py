
#很多时候程序很长，我们不想因为一个错误整个就报错，所以可以利用try-except去避免因为错误导致程序停止运行

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input") #可以看到这里except黄线显示broad，由于错误类型太宽泛

#即第一个try只要错误，就输出invalid input，这并不准确（例如是由于10/0这样的数学错误），可以对except进行分类

try:
    #num = 10/0 如果放在这里，不会有第二次要求输入数字，由于此处赋值已经出现了问题，会直接跳到except中对应的错误
    number = int(input("Enter a number: "))
    num = 10 / 0
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")

#还可以对错误进行命名，之后便于直接输出错误的官方名称

try:
    number = int(input("Enter a number: "))
    num = 10 / 0
    print(number)
except ZeroDivisionError as err_1:
    print(err_1)
except ValueError as err_2:
    print(err_2)