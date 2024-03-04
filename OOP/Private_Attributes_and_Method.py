class Robot:
    def __init__(self, name):
        self.name = name
        # private attribute --> __attribute --> 只能在類別內部存取
        self.__age = 25

    def greet(self):
        # 類別內部可以存取私有屬性
        print(f"Hi, I am {self.__age} years old.")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # private method
    def __this_is_private_method(self):
        print("this is private method.")

    def greet2(self):
        # 類別內部可以存取私有方法
        self.__this_is_private_method()


my_robot = Robot("Wison")
# print(my_robot.__age)  # __age is private attribute
# AttributeError: 'Robot' object has no attribute '__age'
my_robot.greet()  # Hi, I am 25 years old.
print(my_robot.get_age())  # 25
my_robot.set_age(30)
print(my_robot.get_age())  # 30
my_robot.greet2()  # this is private method
