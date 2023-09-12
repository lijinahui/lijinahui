#使用import导入time模块使用sleep功能
# import time
# print("你好")
# time.sleep(5) #通过.就可以使用模块内部的全部功能
# print("我好")

#使用from导入time的sleep功能（函数）
# from    time    import sleep
# print("你好")
# sleep(5)
# print("我好")

#使用*导入time模块的全部功能
# from    time    import *
# print("你好")
# sleep(5)
# print("我好")

#使用as给特定功能加上别名
# import time as t
# print("你好")
# t.sleep(5)
# print("我好")

from time import sleep as s
print("你好")
s(5)
print("我好")

