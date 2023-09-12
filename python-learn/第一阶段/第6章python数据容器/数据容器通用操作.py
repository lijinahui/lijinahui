my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}

#len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串 元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

#max最大元素
print(f"列表 最大元素：{max(my_list)}")
print(f"元组 最大元素：{max(my_tuple)}")
print(f"字符串最大元素：{max(my_str)}")
print(f"集合 最大元素：{max(my_set)}")
print(f"字典 最大元素：{max(my_dict)}")
#min最小元素
print(f"列表 最小元素：{min(my_list)}")
print(f"元组 最小元素：{min(my_tuple)}")
print(f"字符串最小元素：{min(my_str)}")
print(f"集合 最小元素：{min(my_set)}")
print(f"字典 最小元素：{min(my_dict)}")
#类型转换：容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")

#类型转换：容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"符串转元组的结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")

#容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"符串转字符串的结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}")

#容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"符串转集合的结果是：{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是：{set(my_dict)}")

#容器排序
my_list = [3,2,1,4,5]
my_tuple = (4,2,3,1,5)
my_str = "dbcaefg"
my_set = {5,2,3,4,1}
my_dict = {"key4":4,"key2":2,"key3":3,"key1":1,"key5":5}
print(f"列表的排序结果：{sorted(my_list)}")
print(f"元组的排序结果：{sorted(my_tuple)}")
print(f"符串的排序结果：{sorted(my_str)}")
print(f"集合的排序结果：{sorted(my_set)}")
print(f"字典的排序结果：{sorted(my_dict)}")

#反向排序
print(f"列表的反向排序结果：{sorted(my_list,reverse=True)}")
print(f"元组的反向排序结果：{sorted(my_tuple,reverse=True)}")
print(f"符串的反向排序结果：{sorted(my_str,reverse=True)}")
print(f"集合的反向排序结果：{sorted(my_set,reverse=True)}")
print(f"字典的反向排序结果：{sorted(my_dict,reverse=True)}")

#abc比较abd
print(f"adb大于abc,结果{'abd' > 'abc'}")
#a比较ab
print(f"ab大于a,结果{'ab' > 'a'}")
#A比较a
print(f"a大于A,结果{'a' > 'A'}")
#key1比较key2
print(f"key2大于key1,结果{'key2' > 'key1'}")


