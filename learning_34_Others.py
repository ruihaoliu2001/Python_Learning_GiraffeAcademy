
print("{}乘以{}的结果是{}".format(3, 2, 3*2))

message = "This is a new era."
print(f"{message} he said.")

#if "a" is "a":
  #  print("You are right!")

message1 = message.replace("new", "old")
print(message)
print(message1)
message2 = message.strip("a") # 只能删除头尾的字符
print(message2)

a="rrbbrrddrr"
b=a.strip("r")
print(b)

list1 = [1,2,3]
list1.append(3)
print(list1)

"""
n = int(input())
step = 0
max_number = n
while n != 1:
    if (n % 2 == 0):
        n = n // 2
        step = step + 1
    else:
        n = n * 3 + 1
        step = step + 1
        if (n > max_number):
            max_number = n

print(step)
print(max_number)
"""
"""
list = [1,2,5,6,16,7,9]
list.sort(reverse = True) # 按大小顺序进行逆序排列
#list.reverse()是按place的顺序进行逆序的！！！

print(list)
"""


#[i for i in range(7) if i % 2]

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

# namedtuple
from collections import namedtuple

Point = namedtuple("point", field_names=("x", "y"))
p = Point(1,2)
print(p)

print(p.x, p.y)
print(p[0], p[1])


x = 4
y = 9
x, y = y, x
print(x,y)

def swap(x, y):
    return y, x
a, b = swap(1,2)
print(a,b)

def squared(x):
    return x*x
print([squared(x) for x in range(10)])
# map函数，将列表映射到另一个表
print(list(map(squared,(1,2,3,4,5,6))))
#map内的函数不需要加()

#lambda函数，当函数名不重要时
print(list(map(lambda x: x*x, (1,2,3,4,5,6))))

#函数的名字空间（全局变量与局域变量）
x = 1
def scope():
    x = 2
scope()
print(x) # 1

def gscope():
    global x
    x = 2
gscope()
print(x) # 2
# 但这不是纯函数，纯函数指仅使用了input，且该input仅对该return的值有意义
# 不推荐该方法

#函数的递归
def div2(n):
    if n <= 1:
        print(1)
    else:
       print(n)
       div2(n // 2)

div2(123)

#函数的说明文档与help
def square(x):
    "对变量进行平方"
    return x*x
help(square)

def square_1(x):
    """
    对变量进行平方
    x -> x^2
    """
    return x*x
help(square_1)

help(None)

s = "今天的气温是 30 摄氏度，明天是 29 摄氏度"
print(s.count("度"))
print(s.startswith("今"))
print(s.split("，"))

