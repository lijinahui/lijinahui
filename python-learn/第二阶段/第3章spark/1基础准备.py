"""

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspark
"""
#
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf类对象创建Spark Context对象
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)
# 停止Spark Context对象的运行（停止PySpark程序）
sc.stop()