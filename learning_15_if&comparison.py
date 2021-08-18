
def max(num1,num2,num3):
    if num1 >= num2 and num1 >= num3: #比较实际输出的是Bool，即Ture or False
        print(num1)
    elif num2 >= num1 and num2 >= num3:
        print(num2)
    else:
        print(num3)

    if "a" == "a":           #注意如果前面输出数字的print用的是retrun，此处的代码就不运行了，由于return意味着函数的结束。
                             #return是使整个函数返回的，后面的不管是循环里面还是循环外面的都不执行。也即函数第一次运行到某个return便返回，终止运行。
        print("a = a")
    if "a" != "b":
        print("a != b")

max(30,9,5) #运行函数