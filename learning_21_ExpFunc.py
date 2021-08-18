def raise_to_power(cardinal, exponent):
    result = 1
    for index in range(exponent):
        result = result * cardinal
    return result

print(raise_to_power(float(input("Enter cardinal: ")), int(input("Enter exponent: "))))
#注意，由于函数是return值，如果不print，是无法显示结果的