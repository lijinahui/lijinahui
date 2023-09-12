# 演示if elif else 多条件判断语句


# 通过if判断，可以使用多条件判断
# if int(input("请输入你的身高（cm）")) < 120:
#     print("身高小于120cm,可以免费")
# elif int(input("请输入你的vip等级（1-5）：")) > 3:
#     print("vip级别大于3，可以免费游玩。")
# elif int(input("请告诉我今天几号")) == 1:
#     print("今天是1号免费日，可以免费")
# else:
#     print("不好意思，所有条件不满住，需要购票10元")
# print("祝您游玩愉快")

if int(input("请输入第一次猜想的数字")) == 120:
    print("恭喜你答对啦")
elif int(input("不对再猜一次")) == 120:
    print("恭喜你答对啦")
elif int(input("不对，再猜最后一次")) == 120:
    print("恭喜你答对啦")
else:
    print("sorry,全部猜错啦，我想得是120")