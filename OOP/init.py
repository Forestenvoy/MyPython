class Robot:
    # Python 不支援多個建構子，只會載入最後一個
    def __init__(self):
        print("I am a constructor")
    # self 代表物件本身

    def __init__(self, name, age):
        print("I am also a constructor")
        self.name = name
        self.age = age


my_robot_1 = Robot("Wison", 30)  # self = my_robot_1
my_robot_2 = Robot("Grace", 26)  # self = my_robot_2
print(my_robot_1.name, my_robot_1.age)  # Wison 30
print(my_robot_2.name, my_robot_2.age)  # Grace 26


class myclass:
    # in classes, we can also define docstring
    """
    This is a docstring -- 我是 class 的 說明文件
    """


print(myclass.__doc__)  # Returns the docstring
# This is a docstring -- 我是 class 的 說明文件
