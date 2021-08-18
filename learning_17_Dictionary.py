
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
#key必须是不可更改的，所有list不能作为key，tuple可以

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

print(month_convert.keys())
print(month_convert.values())
print(month_convert.items())
#以上前方都会有dict_xxx()输出





li = []
li.append("手机")
li.append("充电器")
li.append("身份证")
li.append("钥匙")
li.append("电脑")

for i in li: # 可以使用 for 依次取出
    print(f"出门之前，别忘了带{i}")

print("女朋友" in li)

stu = {
    "物理": 42,
    "工物": 34,
    "数学": 3,
}
stu_it = stu.items()
print(stu_it) #默认输出前方带有dict_items()
for k,v in stu.items():
    print(f"{k}有{v}选课")

print("数" in stu) #False
print("数学" in stu) #True
print(stu.get("英语", "0"))

# defaultdict
from collections import defaultdict

dsc = defaultdict(int) # 系统默认生成一个字典，对应的value类型为int
dsc["工物"] = 42
dsc["物理"] = 52
dsc["数学"] = 3
dsc[123] = 4
print(dsc["yingyu"])
print(dsc["数学"])
print(dsc[123])


# Counter
deps = ["物理","物理","工物","工物","物理"]
numbers = defaultdict(int)

for d in deps:
    numbers[d]+=1
print(numbers)
#等价于

from collections import Counter

cnumbers = Counter(deps)
print(cnumbers)
print(cnumbers["物理"])


