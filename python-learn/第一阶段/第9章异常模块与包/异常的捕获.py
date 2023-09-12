# # 基本的异常捕获
# try:
#     open("D:/abc.txt","r",encoding="UTF-8")
# except:
#     print("出现异常了，文件不存在，改为w方式打开")
#     f = open("D:/abc.txt","w",encoding="UTF-8")
#
# #捕获多个异常
# try:
# #    1 / 0
#     print(name)
# except NameError as e:
#     print("出现了变量未定义异常")
#     print(e)
# #未正确设置捕获异常类型，将无法捕获
# try:
#     print(name)
#     1 / 0
# except (NameError, ZeroDivisionError) as e:
#     print("出现了变量异常或者除以0异常")
import fileinput

#捕获所有异常
# try:
#     1 / 1
#   #  print(name)
#    # open("D:/456.txt","r")
# except Exception as e:
#     print("出现异常了")
#     print(e)
# else:
#     print("没有异常")


#finally无论是否异常，都执行
try:
    1 / 1
  #  print(name)
   # open("D:/456.txt","r")
except Exception as e: #有异常执行
    print("出现异常了")
    print(e)
else:                   #没异常执行
    print("没有异常")
finally:                #有没有异常都执行
    print("我是finally，有没有都执行")
