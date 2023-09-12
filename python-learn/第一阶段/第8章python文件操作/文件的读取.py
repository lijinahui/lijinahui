# #打开文件
# import time
#
# f = open("D:/测试.txt","r",encoding="UTF-8")
# #print(type(f))
#
# #读取文件 - read()
# #print(f"读取2个字节结果：{f.read(2)}")
# #print(f"读取全部字节结果：{f.read()}")
#
# #读取文件 - readLines
# #lines = f.readlines() #读取文件全部行，封装到列表
# #print(f"lines对象的类型：{type(lines)}")
# #print(f"lines对象的内容：{lines}")
#
# #读取文件 - readline
# #line1 = f.readline()
# #line2 = f.readline()
# #print(f"读取一次{line1}")
# #print(f"读取两次{line2}")
#
# #for循环读取文件行
# for line in f:
#     print(f"每一行数据是{line}")
#
# #文件的关闭close
# f.close()
#
# #with open 语法操作文件
# with open("D:/测试.txt","r",encoding="UTF-8") as f:
#     for line in f:
#         print(f"每一行数据是{line}")
# #time.sleep()

# #1读取全部内容
f = open("D:/测试.txt","r",encoding="UTF-8")
# content = f.read()
# count = content.count("python")
# print(f"python在文件中出现了：{count}次")

#2一行行读取
count = 0
for line in f:
    line = line.strip() #去除开头和结尾的空格及换行
    words = line.split(" ")
    for word in words:
        if word == "python":
            count += 1
print(f"python出现的次数是：{count}")


f.close()



