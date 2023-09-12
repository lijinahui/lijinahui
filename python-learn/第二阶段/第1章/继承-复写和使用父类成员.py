
class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("开启cpu单核")
        # # 方式1 调用父类成员
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        # 方式2
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭cpu单核，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)
