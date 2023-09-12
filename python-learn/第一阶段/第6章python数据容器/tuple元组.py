#定义元组
#可以容纳多个数据，可以容纳不同数据类型，数据是有序存储的，允许重复数据，不可以修改，支持for循环
t1 = (1,"hellow",True)
t2 = ()
t3 = tuple()
t4 = ((1,2,3),(4,5,6),"lijianhui","lijianhui", [123])
print(t4)
#下标索引取内容
num = t4[1]
print(f"从嵌套元组中取结果是：{num}")
#元组的操作：index查找
index = t4.index("lijianhui")
print(f"在t4元组中查找1，的下标是{index}")
#count统计方法
num = t4.index("lijianhui")
print(f"在元组中统计李建辉数量有：{num}个")
num = len(t4)
print(f"在元组中元素有：{num}个")
#元组的遍历
index = 0
while index < len(t4):
    print(f"元组的元素有：{t4[index]}")
    index += 1

for element in t4:
    print(f"2元组的元素有：{element}")

#修改元组不可以
#t4[0] = "1"
#可以修改元组中的list
print(f"t4的内容是：{t4}")
t4[-1][0] = 66
print(f"t4的新内容是：{t4}")
