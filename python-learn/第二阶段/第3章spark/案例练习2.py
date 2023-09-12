import json
import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python-3.10.4\python.exe"
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建Spark Context对象
sc = SparkContext(conf=conf)

# TOD0 需求1：城市销售额排名
# 1.1读取数据文件
file_rdd = sc.textFile("D:/orders.txt")

# 1.2取出一个json字符串
json_str_add = file_rdd.flatMap(lambda X: X.split("|"))

# 1.3将一个json字符串转为字典
dict_rdd = json_str_add.map(lambda X: json.loads(X))

# 1.4 取出城市和销售额数据
# 城市，销售额
city_with_money_rdd = dict_rdd.map(lambda X:(X['areaName'], int(X['money'])))

# 1.5 按城市分组按销售聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a,b: a + b)

# 1.6 按销售额集合结果进行排序
result1_rdd = city_result_rdd.sortBy(lambda X: X[1], ascending=False, numPartitions=1)
print("需求1的结果：", result1_rdd.collect())

# 需求2：全部城市有哪些商品类别在售卖
# 2.1 取出全部的商品类别
category_add = dict_rdd.map(lambda X: X['category']).distinct()
print("需求2 的结果：",category_add.collect())
# 对商品类别进行去重

# 需求3：北京有哪些商品在售卖
# 过滤北京的数据
beijing_data_rdd = dict_rdd.filter(lambda X: X['areaName'] == '北京')

# 3.2 取出全部商品类别
result3 = beijing_data_rdd.map(lambda X: X['category']).distinct()
print("需求3的结果：", result3.collect())








