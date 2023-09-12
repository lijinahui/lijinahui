#
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建Spark Context对象
sc = SparkContext(conf=conf)

# 通过parallelize方法将python对象加载到spark内，成为rdd对象
# rdd1 = sc.parallelize([1,2,3,4,5])
# rdd2 = sc.parallelize((1,2,3,4,5))
# rdd3 = sc.parallelize("asdfg")
# rdd4 = sc.parallelize({1,2,3,4,5})
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})
#
# # 如果要查看rdd里面有什么内容，需要用collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())


# 用过textFile方法，读取文件数据加载到spark内，成为rdd对象
rdd = sc.textFile("D:\python\python-learn\python-learn\第二阶段\第3章spark\hello.txt")
print(rdd.collect())

sc.stop()