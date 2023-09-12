# 定义一个类，内含私有成员变量和私有成员方法
class Phone:
    __current_voltage = 1

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话开启")
        else:
            print("电量不足，无法使用5G，并设置为单核运行")

phone = Phone()
phone.call_by_5g()

class Android:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G开启")
        else:
            print("5g关闭，使用4g")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
android = Android()
android.call_by_5g()