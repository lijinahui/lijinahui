fr = open("D:/bill.txt","r",encoding="UTF-8")
fw = open("D:/bill.bak.txt","w",encoding="UTF-8")

for line in fr:
    line = line.strip() #去除空格和换行
    if line.split(",")[-1] == "测试":
        continue #进入下一次循环，这一次的后面内容跳过
    fw.write(line)
    fw.write("\n")
fr.close()
fr.close()








