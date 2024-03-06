class Robot:
    def __init__(self, name):
        self.name = name
        self.__age = 25

    # 透過 getter/setter 去設定私有屬性
    # 注意 !!! 先寫 getter 再寫 setter

    # 新寫法
    # @property 的裝飾器，Property 立刻就讓資料變成只能取用，不能更新或者刪除
    @property
    def age(self):
        return self.__age

    # 新寫法
    @age.setter
    def age(self, age):  # setter 嚴格檢測變更值是否合法
        if 0 < age < 100:
            self.__age = age
        else:
            print("age must between 0 and 100")

    @age.deleter  # 刪除私有屬性
    def age(self):
        del self.__age

    # 傳統寫法
    def age_getter(self):  # getter
        return self.__age

    # 傳統寫法
    def age_setter(self, age):  # setter 嚴格檢測變更值是否合法
        if age > 0 and age < 100:
            self.__age = age
        else:
            print("age must between 0 and 100")


my_robot = Robot("Wison")
my_robot.age_setter(30)
print(my_robot.age_getter())  # 30
my_robot.age = 35
print(my_robot.age)  # 35
