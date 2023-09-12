"""
演示面向对象：继承的基础语法
"""
# 演示单继承
class Phone:
    IMEI = None
    producer = "HM"

    def call_by_4g(self):
        print("4g")

class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022年新功能，5g")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")

class MyPhone(Phone, NFCReader, RemoteControl):
    pass

phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()


