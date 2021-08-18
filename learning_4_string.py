print("gir\\affe\"academy\naaa")

phrase ="Giraffe Academy"
print("\n"+phrase + " is cool" + "\n")

print(phrase.lower() + " lower\n")
print(phrase.upper() + " upper\n")

#phrase.upper() 等操作并没有改变字符串本身，只是暂时输出相应的内容
# phrase = phrase.upper() 这样就可以改变phrase本身了

print(phrase) #以上的操作并没有改变字符串本身，只是暂时输出相应的内容
print(phrase.islower(),"\n")
print(phrase.isupper(),"\n")

print(phrase.upper().isupper(),"\n")

print(len(phrase)) # print(phrase.len()) is wrong

print(phrase[0] + phrase[1])    # start from 0，字符串可以直接相加来合并

print(phrase.index("f")) # only find the one that first appears

print(phrase.replace("Giraffe","fuck"))

# 综上，phrase.xxx()函数均输出关于原string的相关改动（仍是string）；而len(string)这种输出的与string无关了。
# 以上的phrase相当于C语言中的字符串，所以可以用phrase[]来选取某个元素
