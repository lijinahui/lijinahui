"""
# 图形化DBeaver
# SQL单行注释：-- 注释内容（--后面有空格）
# SQL单行注释：# 注释内容
# 多行注释：/* 注释内容 */

DDL 库的创建删除，表的创建删除

DML 新增，删除，修改数据
插入insert    删除delete    更新update

DQL 基于需求查询和计算数据
select 列 from 表 where 条件；
分组聚合group by
select 字段|聚合函数 from 表 [where 条件] group by 列 ;
select gender,avg(age),sum(age),min(age),max(age),count(age) from student group by gender;
排序分页order by
select * from student where age > 20 order by age(默认的，从小到大)|desc(从大到小)；


DCL 新增，删除，用户。密码修改，权限管理
"""







