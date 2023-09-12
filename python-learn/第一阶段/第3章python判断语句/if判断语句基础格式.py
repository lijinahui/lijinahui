"""
演示python判断语句：if语句的基本格式应用
"""
age = 10
if age >= 18:
    print("我已经成年了")
print("时间过得真快啊")

age = input("请告诉我你的年龄")
if int(age) >= 18:
    print("您已成年，游玩需要补票10元")
else:
    print("您未成年，可以正常游玩")
print("祝您游玩愉快")