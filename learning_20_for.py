
for letter in "Giraffe Academy": # in是python独有的一个工具
    print(letter)

friends = ["Andy", "Raymond", "Candy", "Liu",3]
for friend in friends:
    print(friend)

for index in range(5, 10): #从5到10的所有整数，不包括10
    print(index)

for index in range(len(friends)):  #len函数对str, list, dictionary都管用
    print(friends[index])

for index in range(5): #range: 0 -- range-1
    if index == 0:
        print("First iteration")
    else:
        print("Not first")

# python中的for基本都要配合in使用，如果需要判断，一般用while


