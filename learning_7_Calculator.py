num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result_1 = int(num1) + float(num2) #字符串的直接合并，注意若int，输入的是float会报错
#默认input的是str形式
result_2 = num1 + num2 # 字符串可以直接相加作为合并

print(result_1) #数字相加

print(result_2) #数字叠放在一起