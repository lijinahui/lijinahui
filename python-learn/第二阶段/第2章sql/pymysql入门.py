# pymysql库的基础操作

from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="39.97.110.1",     # ip
    port=3306,              # 3306
    user="root",            # 账户
    password="123456",      # 密码
    autocommit=True         # 设置自动提交
)
# print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()      # 获取游标对象
conn.select_db("test")      # 选择数据库
# cursor.execute("create table test_pymysql2(id int)")

# 执行sql
cursor.execute("insert into student values(10,'环境',32)")
# 执行查询性质SQL
cursor.execute("select * from student")

results= cursor.fetchall()
for l in results:
    print(l)


# 关闭链接
conn.close()




