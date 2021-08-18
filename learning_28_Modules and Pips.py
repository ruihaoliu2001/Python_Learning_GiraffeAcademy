

# Module实际上是一些已经写好的python文件，可以在现在正在编写的文件中直接调用
# 事实上，我们python里许多现成的函数就是一个个module

#import learning_28_Asistance_for_28 # 引入该文件，可以使用其中已经定义好的功能
#print(learning_28_Asistance_for_28.roll_dice(6)) #如果没有前面原始python文件名.xxx，import一行会是灰色

#第二种书写方式：
from learning_28_Asistance_for_28 import roll_dice
print(roll_dice(6))


#在External Library的python3.9里面，有许多已经下载好的module，其他可以在Terminal里面利用Pip install xxx来直接下载，会下载到site-package中





