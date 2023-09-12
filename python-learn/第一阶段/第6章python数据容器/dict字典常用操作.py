#
# my_dict = {"王力宏":99,"周杰伦":88,"林俊杰":77}
# #新增
# my_dict["张信哲"] = 66
# print(f"字典新增元素后{my_dict}")
#
# #更新
# my_dict["周杰伦"] = 33
# print(f"字典更新元素后{my_dict}")
#
# #删除元素
# score = my_dict.pop("周杰伦")
# print(f"字典移除元素后{my_dict}，移除的周杰伦分数是：{score}")
#
# #清空元素，clear
# my_dict.clear()
# print(f"字典被清空了，结果是{my_dict}")
#
# #获取全部key
# my_dict = {"王力宏":99,"周杰伦":88,"林俊杰":77}
# keys = my_dict.keys()
# print(f"字典全部的key是{keys}")
#
# #遍历字典
# #方式1
# for i in keys:
#     print(f"字典的key是:{i}")
#     print(f"字典的value是:{my_dict[i]}")
#
# #方式2
# for key in my_dict:
#     print(f"2字典的key是:{key}")
#     print(f"2字典的value是:{my_dict[key]}")
#
# #统计字典内的元素数量
# num = len(my_dict)
# print(f"字典的元素数量有：{num}个")
#

info_dict = {
    "王力宏": {
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    }
}
print(f"全体员工信息：{info_dict}")
#for循环遍历字典
for name in info_dict:
    #if条件判断符合条件的员工
    if info_dict[name]["级别"] == 1:
        #升加操作，获取员工字典
        employee_info_dict = info_dict[name]
        #修改员工字典
        employee_info_dict["级别"] = 2 #级别+1
        employee_info_dict["工资"] += 1000 #工资+1000
        #将员工信息更新回info_dict
        info_dict[name] = employee_info_dict
#输出结果
print(f"升加后结果{info_dict}")
