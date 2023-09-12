#无return语句的函数返回值
def say1():
    print("nihao")
result = say1()
print(f"无返回函数，返回内容是：{result}")
print(f"无返回函数，返回的内容类型是：{type(result)}")
#主动返回None
def say2():
    print("nihao")
    return None
result = say2()
print(f"无返回函数，返回内容是：{result}")
print(f"无返回函数，返回的内容类型是：{type(result)}")
#None用于if
def check_age(age):
    if age > 18:
        return "success"
    else:
        return None
result = check_age(20)
if not result:
    print("未成年，不可以进入")
else:
    print("请进")
#None用于声明无初始值内容的变量
name = None


