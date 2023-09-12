#函数内修改的变量值，不影响函数外的值

num =200
def a():
    print(f"a:{num}")
def b():
    num = 500
    print(f"b:{num}")
a()
b()
print(num)

#global关键字，函数内部定义的变量为全局变量

num =200
def a():
    print(f"a:{num}")
def b():

    global num
    num = 500
    print(f"b:{num}")

a()
b()