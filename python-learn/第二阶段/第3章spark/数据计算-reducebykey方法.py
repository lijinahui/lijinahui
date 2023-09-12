# 功能：针对KV型rdd,自动按照key分组，然后根据你提供的聚合逻辑，完成组内数据的聚合操作
# 接受两个传入参数（类型要一致），返回一个返回值，类型和传入要求一致
# func: (V, V) -> V

import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python-3.10.4\python.exe"
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建Spark Context对象
sc = SparkContext(conf=conf)

# 准备一个rdd
rdd = sc.parallelize([('男', 99), ('男', 88), ('女', 99), ('女', 66)])
# 求男生和女生两个组的成绩和
rdd2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())
