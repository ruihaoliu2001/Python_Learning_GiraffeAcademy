
coordinates = (4,5) #tuble

print(coordinates)
print(coordinates[1])

# coordinates[1] = 10 这样的操作不被允许，tuble是不可更改的，这是tuble和list的区别之一

group = [(4, 5), (3, 7), (10, 23)]
print(group[1])

#总的来说，tuble主要用于存储常量，即不再会被改变的量
coordinates = coordinates + (0,)
print(coordinates)

list = [0]
print(list)

tuple = (0)
print(tuple) #打印出了数字int 0

tuple_1 = (0,)
print(tuple_1) #打印出了数字(0,)，是一个tuple



# namedtuple
from collections import namedtuple

Point = namedtuple("point", field_names=("x", "y"))
p = Point(1,2)
print(p)

print(p.x, p.y)
print(p[0], p[1])