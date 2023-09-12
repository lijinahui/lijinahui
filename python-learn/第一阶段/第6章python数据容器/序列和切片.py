#对list进行切片，从1开始，4结束，步长1
my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]
print(f"结果1：{result1}")
#对tuple进行切片，从头开始，到最后结束，步长1
my_tuple = (0,1,2,3,4,5,6)
result2 = my_tuple[:]
print(f"结果2：{result2}")
#对str进行切片，从头开始，到最后，步长2
my_str = "0123456"
result3 = my_str[::2]
print(f"结果3：{result3}")
#对str进行切片，从头开始，到最后结束，步长-1
my_str = "0123456"
result4 = my_str[::-1]
print(f"结果4：{result4}")
#对列表进行切片，从3开始，到1结束，步长-1
my_list = [0,1,2,3,4,5,6]
result5 = my_list[1:3:1]
print(f"结果5：{result5}")
#对元组进行切片，从头开始，到尾结束，步长-2
my_tuple = (0,1,2,3,4,5,6)
result6 = my_tuple[::-2]
print(f"结果6：{result6}")

my_str = "万过薪月，员序程马黑来，nohtyP学"

result7 = my_str[9:4:-1]
print(f"结果7：{result7}")
result8 = my_str.split("，")[1].replace("来","")[::-1]
print(f"结果6：{result8}")