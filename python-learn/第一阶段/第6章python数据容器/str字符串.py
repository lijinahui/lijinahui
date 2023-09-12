#通过下标索引取值
my_str = "itheima and itcast"
value =my_str[2]
value2 =my_str[-2]
print(f"从字符串取下第二个值是{value},取下倒数第二个值是：{value2}")
#index方法
value = my_str.index("an")
print(f"在字符串查找an，起始下标是：{value}")

#字符串.replace字符1，字符2。替换并得到一个新的字符串，不是修改哦
new_my_str  = my_str.replace("it","程序")
print(f"将字符串{my_str}替换后得到：{new_my_str}，类型是：{type(my_str)}")

#字符串.split(分割符字符串），字符串本身不变，得到一个列表对象
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list}，类型是：{type(my_str_list)}")

#strip方法
my_str = "12hello python itheima     itcast21"
new_my_str = my_str.strip()
print(f"字符串{my_str}被strip后，结果：{new_my_str}")
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip后，结果：{new_my_str}")

#统计字符串中某字符串的出现次数
count = my_str.count("it")
print(f"长度为：{count}")
#统计字符串长度
num = len(my_str)
print(f"长度是：{num}")


#练习
my_str = "itheima itcase boxuegu"
num = my_str.count("it")
print(f"有{num}个it字符")
new_my_str = my_str.replace(" ", "|")
print(f"替换后是：{new_my_str}")
new_my_str = my_str.split("|")
print(f"|分割后的字符是：{new_my_str}")








