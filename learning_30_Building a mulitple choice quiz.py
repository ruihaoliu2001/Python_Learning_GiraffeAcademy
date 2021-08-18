
from learning_30_Question import Question #导入Question class

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Green\n(c) Purple\n\n",
    "What color are grapes?\n(a) Red\n(b) Green\n(c) Purple\n\n",
    "What color are cucumbers?\n(a) Red\n(b) Green\n(c) Purple\n\n",
] # 所有问题合集

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
] # 所有问题class的构建


def run_test(questions): #注意，这里的questions是一个参数，它与我们前面定义的实际questions不是一个东西，可以从鼠标放到上面不与前面的questions重合知道。
    #这个questions也可以用别的名称替代，这里用了questions可以说明虽然名字一样，但是代表的内容（地址）并不同
    score = 0
    for question in questions:
        answer = input(question.prompt + "Enter your answer: ") #结构体中prompt字符串部分的调用
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")
# 测试程序
# 将我们需要干的每一步写成一个独立的函数最后仅仅简单的调用更规整，也方便大型工程的构建

run_test(questions) #这里的questions才是真正我们定义的questions

# 总的来说，class可以帮助我们很好的存储一个事物的多方面信息，使得代码更规整也更可读


