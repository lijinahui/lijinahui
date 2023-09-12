# 对rdd执行map操作，然后进行解除嵌套操作
# # 嵌套的list
# lst = [[1,2,3], [4,5,6], [7,8,9]]
# # 解除嵌套
# lst = [1,2,3,4,5,6,7,8,9]

import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python-3.10.4\python.exe"
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建Spark Context对象
sc = SparkContext(conf=conf)

# 准备一个rdd
rdd = sc.parallelize(["itheima itcast 666", "itheima itheima itcast", "python itheima"])
rdd2 = rdd.map(lambda X: X.splist(""))

# 需求，将rdd数据里面的一个个单词提取出来

rdd2 = rdd.flatMap(lambda X: X.split(" "))
print(rdd2.collect())