#定义集合(集合允许修改，不允许重复，顺序无法保证，不支持下表索引)
my_set = {"李建辉","创领科技","运维","李建辉","创领科技","运维"}
my_set_empty = set()
print(f"my_set的内容是：{my_set},类型是{type(my_set)}")
print(f"my_set的内容是：{my_set_empty},类型是{type(my_set)}")

#添加新元素
my_set.add("python")
print(f"my_set添加python元素后的内容是：{my_set},类型是{type(my_set)}")

#移除元素
my_set.remove("python")
print(f"my_set移除python元素后的内容是：{my_set},类型是{type(my_set)}")

#随机取出一个元素
element = my_set.pop()
print(f"my_set随机取出的元素是：{element}，取出后的内容是：{my_set}")

#清空集合
my_set.clear()
print(f"my_set被清空了，内容是：{my_set}")

#取2个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print("差集")
print(set3)
print(set1)
print(set2)
print()

#消除2个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print("消除集合的差集")
print(set1)
print(set2)
print()

#2个集合合并为1个
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print("2个集合合并")
print(set3)
print()

#统计集合元素数量len()
set1 = {1,2,3,4,5,1,2,3,4,5,1,2,3,4,5}
num = len(set1)
print(f"集合元素数量有{num}个")
print()

#集合的遍历(不支持下标，不能while,可以for)
set1 = {1,2,3,4,5}
for element in set1:
    print(f"集合的元素有：{element}")


my_list = ['李建辉','创领','运维','李建辉','创领']
my_set = set()
for i in my_list:
    my_set.add(i)
print(f"有列表{my_list}")
print(f"存入集合后的结果{my_set}")
