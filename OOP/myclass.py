class Robot:
    """ This is Robot's docstring """

    # class attribute (類別屬性) --> ingredient
    ingredient = "metal"

    def __init__(self, name, age):
        # constructor
        # Instance Variable（實例變數） --> name, age
        self.name = name
        self.age = age

    def greet(self):
        # 方法內使用 class attribute --> self.__class__.attribute (inside method definition)
        print(
            f"Hi, my name is {self.name}, and I am made of {self.__class__.ingredient}")

    # static method 靜態方法 --> 不需要實體化即可呼叫
    @staticmethod
    def Hello():
        print("Hello, I am static method")


my_robot_1 = Robot("Wison", 30)  # self = my_robot_1
my_robot_2 = Robot("Grace", 26)  # self = my_robot_2

my_robot_1.greet()  # Hi, my name is Wison, and I am made of metal
# 方法外部使用 class attribute --> objectname.attribute or classname.attribute --> 符合 Python 社群的慣例
print(my_robot_1.__class__.ingredient)  # metal  <-- 不推薦
print(my_robot_1.ingredient)  # metal
print(Robot.ingredient)  # metal

# static method 可以直接呼叫，不須實體化
Robot.Hello()  # Hello, I am static method
my_robot_1.Hello()  # Hello, I am static method
