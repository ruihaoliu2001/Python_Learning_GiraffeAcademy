
month_convert = {
"Jan": "January",
"Feb": "February",
"Mar": "March",
"Apr": "April",
"May": "May",
"Jun": "June",
"Jul": "July",
"Aug": "August",
"Sept": "September",
"Oct": "October",
"Nov": "November",
"Dec": "Decmber",
0: "number",
}
#以上的列表叫做Dictionary，左边的是key，右边的是value，即key-value pairs。
#python中列表里的元素也可以有各种类型

print(month_convert["Sept"])
print(month_convert.get("Nov"))
print(month_convert[0])

print(month_convert.get("Luv"))
print(month_convert.get(1))
# print(month_convert[1])这样会报错，而使用.get()则会输出none

#或者：
print(month_convert.get(1, "Invalid"))
print(month_convert.get(0, "Invalid"))
# 如果没找到key，会输出后方的default内容

print(month_convert) #也可以直接以原形式打印出列表本身
print(len(month_convert))



