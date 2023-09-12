# 对rdd数据的排序操作

import os
os.environ['PYSPARK_PYTHON'] = "D:\python\python-3.10.4\python.exe"
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建Spark Context对象
sc = SparkContext(conf=conf)

# 读取数据文件
rdd = sc.textFile("D:/hello.txt")

# 提取全部单词
word_rdd = rdd.flatMap(lambda X: X.split(" "))

# 将所有单词都转换成二元元组，单词为key，value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))

# 分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a,b: a + b)

# 对结果进行排序
final_rdd = result_rdd.sortBy(lambda X: X[1], ascending=True, numPartitions=1)
# 打印输出结果
print(final_rdd.collect())
