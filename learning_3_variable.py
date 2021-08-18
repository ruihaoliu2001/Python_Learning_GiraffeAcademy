character_name = "Tom" # 字符串数据类型
num_age = 35 # 数字数据类型
is_name = False # Bool数据类型

print(is_name)
print(character_name+"'s age is ",num_age, "'s age is ",is_name) # +不起到空格的作用（+前后的空格数对输出无影响，只是好看）
character_name = "Mike" #变量的重新赋值
print(character_name + "'s age is ",num_age) #不同变量类型之间只能用逗号，同类型用逗号和+均可，但是逗号会带来一个空格。
# print可以直接print任意类型的数据（数字，str 或者bool）

print(num_age, character_name, sep="") #sep可以在最后调整不同类型输出之间的间隔

print(num_age, character_name, sep="\n")