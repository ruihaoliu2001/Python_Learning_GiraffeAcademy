
lucky_numbers = [444,8,15,16,32,43]
friends = ["Jim","Candy","Raymond","Kate"]

print(friends)

friends.extend(lucky_numbers) #list之间的合并
print(friends)

friends.append("fuck") #一次仅能添加一个元素
print(friends)

friends.insert(1,"Kevin") #在中间插入元素,第一个参数需要写的是index
print(friends)

friends.remove("fuck") #remove中需要写清楚要去掉的全程，而不是index
print(friends)

friends.clear() #清空list
print(friends)

friends = ["Jim","Candy","Raymond","Raymond","Kate"]
friends.pop() # 去掉列表中最后一个元素，与字符串不同，list的.函数运行后会对list本身有改变
print(friends)

print(friends.index("Raymond")) #给出这一元素所在的位置，会给出第一次出现的位置
# print(friends.index("Raymon")) 若不在列表中，系统会报错

print(friends.count("Raymond")) #计数

friends.sort()
lucky_numbers.sort()
print(friends,lucky_numbers) #按ASCII码顺序升序排列

friends.reverse()
lucky_numbers.reverse()
print(friends,lucky_numbers) #按place的空间顺序降序排列
# 注意：.reverse()函数不如.sort()准确率高

friends_2 = friends.copy() #复制list
print(friends_2)

# 若phrase是字符串string，phrase.upper() 等操作并没有改变字符串本身，只是暂时输出相应的内容
# 若friends是list，则以上这些friedns.xxx()操作均改变了frineds本身
