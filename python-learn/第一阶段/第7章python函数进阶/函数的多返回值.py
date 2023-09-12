# 演示多个变量，多个返回值示例
def test_return():
    return 1, "hello", True
x,y,z = test_return()
print(x)
print(y)
print(z)

# 函数的多种传参
def user_info(name, age, gender):
    print(f"您的名字是：{name},年龄是{age}，性别是{gender}")

#位置参数-默认使用
user_info('小明', 20, '男')

# 关键字参数
user_info(name='小王', gender='女', age=11)

# 缺省参数（默认值）且在最后
def user_info(name, age, gender='男'):
    print(f"您的名字是：{name}, 年龄是{age}， 性别是{gender}")
user_info('小天', '13')

# 位置传递, 不定长, *号
#不定长的定义形式参数会作为元组存在，接受不定长数量的参数传入
def user_info(*args):
    print(f"args参数类型是：{type(args)},内容是：{args}")

user_info('TOM', 18)

#关键字传递，不定长,**号

def user_info(**kwargs):
    print(f"args参数类型是：{type(kwargs)}, 内容是：{kwargs}")
user_info(name='TOM', age=18, id=110)


