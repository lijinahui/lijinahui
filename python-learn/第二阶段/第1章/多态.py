"""
演示面向对象的多态特性以及抽象类（接口）的使用

"""
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
def make_noise(animal: Animal):
    """制造点噪音，需传入Animol对象"""
    animal.speak()
# 演示多态，使用两个子类对像调用函数
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

# 演示抽象类
class AC:
    def coll_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass

class Midea_AC(AC):
    def coll_wind(self):
        print("美的制冷")
    def hot_wind(self):
        print("美的制热")

class Gree_AC(AC):
    def coll_wind(self):
        print("格力制冷")
    def hot_wind(self):
        print("格力制热")

def make_cool(ac: AC):
    ac.coll_wind()
midea_ac = Midea_AC()
gree_ac = Gree_AC()
make_cool(midea_ac)
make_cool(gree_ac)

