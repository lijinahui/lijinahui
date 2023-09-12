"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1，设计一个类，可以完成数据的封装
2，设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3，读取文件，生成数据对象
4，进行数据需求的逻辑计算（计算每一天的销售额）
5，通过pyecharts进行图形绘制
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import  Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
from pymysql import  Connection



text_file_reader = TextFileReader("D:/python/python-learn/python-learn/第二阶段/第1章/数据分析案例/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/python/python-learn/python-learn/第二阶段/第1章/数据分析案例/2011年2月销售数据.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

#将两个合并为1个list
all_data: list[Record] = jan_data + feb_data
print(all_data)


# # 开始数据计算
# data_dict = {}
# for record in all_data:
#     if record.date in data_dict.keys():
#         # 当前日期已经记录，所以和老记录累加即可
#         data_dict[record.date] += record.money
#     else:
#         data_dict[record.date] = record.money
#
# # 可视化
# bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
# bar.add_xaxis(list(data_dict.keys()))   #添加x轴数据
# bar.add_yaxis("销售额", list(data_dict.values()))  #添加y轴数据
# bar.set_global_opts(
#     title_opts = TitleOpts(title="每日销售额")
# )
# bar.render("每日销售额柱状图.html")

# 构建MySQL链接对象
conn = Connection(
    host="39.97.110.1",     # ip
    port=3306,              # 3306
    user="root",            # 账户
    password="123456",      # 密码
    autocommit=True         # 设置自动提交
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("test")
# 组织sql语句
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # 执行sql
    cursor.execute(sql)


    print(sql)
# 关闭MySQL链接对象
conn.close()

















