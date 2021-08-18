
from learning_32_Chef import Chef
from learning_32_ChineseChef import ChineseChef

mychef = Chef() #由于这里原始Chef定义没有__init__，所以不需要在括号中传递参数，写空括号即可
mychef.make_special_dish() #会打印出一句话，由于这个函数的作用就是打印一句哈

print("\n")

my_chinese_chef = ChineseChef()
my_chinese_chef.make_special_dish() # 这里的special_dish就有了修改
my_chinese_chef.make_fried_rice()

# 本质上就是结构体的嵌套（继承）