# 对rdd数据的去重操作

import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python-3.10.4\python.exe"
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建Spark Context对象
sc = SparkContext(conf=conf)

# 准备一个rdd
rdd = sc.parallelize([1,2,3,3,5,6,6,7,8,9])

# 对rdd的数据进行去重
rdd2 = rdd.distinct()
print(rdd2.collect())