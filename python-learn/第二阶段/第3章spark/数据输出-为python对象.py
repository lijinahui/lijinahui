import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python-3.10.4\python.exe"
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建Spark Context对象
sc = SparkContext(conf=conf)

# 准备一个rdd
rdd = sc.parallelize([1,2,3,4,5])

# collect算子
