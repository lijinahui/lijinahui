"""
文件处理相关的
"""
def print_file_info(file_name):
    """
    功能是将给定路径的文件内容输出到控制台
    :param file_name: 即将读取的文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name,"r",encoding="UTF-8")
        content = f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"(程序异常了，原因是：{e}")
    finally:
        if f:   #如果变量是None，表示False,如果有任何内容，就表示True
            f.close()
def append_to_file(file_name,data):
    """
    功能将指定的数据追加到指定文件
    :param file_name: 指定文件路径
    :param data: 指定数据
    :return: None
    """
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    #print_file_info("D:/bill.txtxxx")
    append_to_file("D:/test_append.txt","hahaha")




