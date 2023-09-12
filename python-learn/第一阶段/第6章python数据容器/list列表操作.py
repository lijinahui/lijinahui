"""
演示数据容器之：list列表

"""
#定义一个列表list
my_list = ["itheima","lijianhui","123"]
print(my_list)
# print(type(my_list))
# print()
# print(my_list[0][-1])
index = my_list.index("123")
print(f"123在列表中的下标索引是：{index}")
#修改特定下标的索引值
my_list[2] = "yangshuangshuang"
print(f"列表被修改后元素值是：{my_list}")
#在指定下标位置插入新元素
my_list.insert(2,"ai")
print(f"列表插入元素后，结果是：{my_list}")
#在列表尾部追加元素
my_list.append("!!!")
print(f"列表追加元素后，结果是：{my_list}")
#在列表尾部追加一批新元素
my_list2 = ["1","1","2","3"]
my_list.extend(my_list2)
print(f"列表追加新的列表后，结果是：{my_list}")
#删除方式1，del 列表【下标】
del my_list[-1]
print(f"通过del删除的列表后，结果是：{my_list}")
#方法2：列表.pop（下标）
element = my_list.pop(-1)
print(f"通过pop方法删除的列表后，结果是：{my_list},取出的元素是{element}")

#统计某个元素在列表中的数量
count = my_list.count("1")
print(f"列表中1的数量是：{count}")
#统计列表内的全部元素数量
count = len(my_list)
print(f"列表中的元素数量总共是：{count}")
#删除某元素在列表中的第一个匹配项
my_list.remove("1")
print(f"通过remove方法移除元素后，列表的结果是：{my_list}")
#清空列表内容
my_list.clear()
print(f"列表被清空了，结果是：{my_list}")