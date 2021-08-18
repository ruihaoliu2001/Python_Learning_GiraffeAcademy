
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1]) #结果是8

print("/////")

for row in number_grid:
    for col in row:
        print(col)

print("/////")
#等价于下面这一稍微麻烦一点的方式
for row in number_grid:
    for index in range(len(row)):
        print(row[index])
