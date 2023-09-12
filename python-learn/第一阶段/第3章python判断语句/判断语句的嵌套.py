"""
演示判断语句的嵌套使用
"""
# if int(input("你的身高是多少：")) > 120:
#     print("身高超出限制，不可以免费")
#     print("但是，如果VIP级别大于3，可以免费")
#
#     if int(input("你的VIP级别是多少：")) > 3:
#         print("恭喜你，VIP级别达标，可以免费")
#     else:
#         print("sorry 你需要买票10元")
# else:
#     print("欢迎你小朋友，可以免费游玩")

# age = 8
# year = 1
# level = 6
# if age >= 18:
#     print("你是成年人")
#     if age  < 30:
#         print("你的年龄达标了")
#         if year > 2:
#             print("恭喜你，年龄和入职时间都达标，可以领取礼物")
#         elif level > 3:
#             print("恭喜你，年龄和级别达标，可以领礼物")
#         else:
#             print("不好意思，尽管年龄达标，但是入职时间和级别都不达标。")
#     else:
#         print("不好意思，年龄太大了")
# else:
#     print("不好意思，小朋友不可以领取")

"""
演示判断语句案例：终极猜数字（后续用循环语句优化）
"""
# 1.构建一个随机数变量
import random
num = random.randint(1,10)
guess_num = int(input("输入你要猜测的数字："))
#2.通过if判断语句进行语句数字的猜测
if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")
    guess_num = int(input("第二次输入你猜测的数字："))
    if guess_num == num:
        print("恭喜，第二次猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")
        guess_num = int(input("第三次输入你猜测的数字："))
        if guess_num == num:
            print("第三次猜中了")
        else:
            print("三次机会用完了，没有猜中。")