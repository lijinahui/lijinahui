# def list_while_func():
#     my_list = ["黑马","李建辉","杨双双"]
#     index = 0
#     while index < len(my_list):
#         element = my_list[index]
#         print(f"列表的元素：{element}")
#         index += 1
#
#
# def list_for_func():
#     my_list = [11,2,3]
#     for element in my_list:
#         print(f"列表的元素有：{element}")
#
# list_for_func()
#
# list_while_func()
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = []
index = 0
while index < len(list_1):
    element = list_1[index]
    if element % 2 == 0:
        list_2.append(element)
    index += 1


