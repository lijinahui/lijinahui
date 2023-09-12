import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python-3.10.4\python.exe"
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建Spark Context对象
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1,2,3,4,5])

# 通过map方法将全部数据都乘以10
# def func(data):
#     return data * 10
# rdd2 = rdd.map(func)
rdd2 = rdd.map(lambda X: X * 10)


 # (T) -> U
 # (T) -> T

# 链式调用
# rdd3 = rdd2.map(lambda X: X+ 5)
rdd2 = rdd.map(lambda X: X * 10).map(lambda X: X + 5)

print(rdd2.collect())
