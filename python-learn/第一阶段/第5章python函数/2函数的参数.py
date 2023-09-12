# def add(x,y):
#     result = x + y
#     print(f"{x} + {y}的计算结果是：{result}")
# add(1, 2)
# add(56,37)

def add(x):
    if x <= 37.5:
        print(f"欢迎来到黑马，\n体温测量中，您的体温是{x}，体温正常请进")
    else:
        print(f"欢迎来到黑马，\n体温测量中，您的体温是{x}，需要隔离")

add(38)
add(35)
