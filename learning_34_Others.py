
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

list = [1,2,5,6,16,7,9]
list.sort(reverse = True) # 按大小顺序进行逆序排列
#list.reverse()是按place的顺序进行逆序的！！！

print(list)

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