# 打开文件，不存在的文件，r,w,a
import time

f = open("D:/test.txt","a",encoding="UTF-8")
# #write写入
# f.write("Hello") #内容写入到内存中
# f.flush() #将内存中内容，写入到硬盘
# f.close() #close方法，内置了flush的功能

###文件的追加写入
f.write("\n456") #换行追加\n
f.close()






