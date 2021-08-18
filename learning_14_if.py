is_male = True
is_tall = True

if is_male:
    print("You are a male!")  #所有缩进的都认为是if的语句

is_male = False
if is_male:
    print("You are not a male!") #不工作，由于判断为False

if is_male:
    print("You are a male!")
else:
    print("You are not a male!")


is_male = False
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both!")
else:
    print("You are neither a male nor tall!")

is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a male and tall!")
else:
    print("You are not a male or not tall or both!")

if is_male and is_tall:
    print("You are a male and tall!")
elif is_male and not(is_tall):
    print("You are a male and not tall!")
elif not(is_male) and is_tall:
    print("You are not a male and tall!")
else:
    print("You are neither a male nor tall!")

if is_male:
    if is_tall:
        print("You are handsome!")
    else:
        print("You are not handsome!")
elif is_tall:
    print("You are beautiful!")
else:
    print("You are not beautiful!") #类似惯常C语言的写法