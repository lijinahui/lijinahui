"""
演示面向对象类中的成员方法定义和使用
"""

# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f"大家好，我是{self.name}，欢迎大家多多关照")
    def say_hi2(self,msg):
        print(f"大家好，我是{self.name}，{msg}")

stu = Student()
stu.name = "周杰伦"
stu.say_hi()

stu2 = Student()
stu2.name = "林俊杰"
stu2.say_hi2("小伙哦，我看好你")
