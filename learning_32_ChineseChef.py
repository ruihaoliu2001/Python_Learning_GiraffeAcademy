
from learning_32_Chef import Chef

class ChineseChef(Chef): # 结构体的继承，这样新的结构体就拥有了原来结构体的所有功能

    def make_fried_rice(self):
        print("The chef makes fried rice!")

    #如果我们想对新的结构体的旧功能有所修改：
    def make_special_dish(self):
        print("The chef makes orange juice!")
    # 这样就从原先的special dish更改成了orange juice

    # 本质上就是结构体的嵌套（继承）