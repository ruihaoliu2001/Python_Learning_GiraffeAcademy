
# target: Any vowel(a,e,i,o,u) -> g

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translator(input("Enter a phrase: ")))

#一些优化：
def translator_1(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #不用判断大写了
            if letter.isupper():
                translation = translation + "G"   #可以将大写字母仍变成大写字母
            else:
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translator_1(input("Enter a phrase: ")))