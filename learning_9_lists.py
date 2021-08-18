

friends_1 = ["Jim","Candy","Raymond"]
friends_2 = ["Jim",2,False] #可以允许不同元素在同一个列表当中
friends_1[1] = "Candyy"

print(friends_1) #可以直接带着中括号print出整个list
print(friends_2)

print(friends_1[2])
print(friends_2[-1]) #从尾部开始的话，第一个编号为-1

print(friends_1[0:2]) #包括0元素，直到2之前的最后一个元素
