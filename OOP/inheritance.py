# 繼承 實作

class People:  # 父類別 People
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping ...")

    def eat(self):
        print(f"{self.name} is eating rice...")


class Student(People):  # 子類別 Student <-- 繼承 父類別 People
    def __init__(self, name, age, student_id):
        # super() 會繼承父類別的 __init__() 方法
        super().__init__(name, age)
        self.student_id = student_id

    # 覆寫 Override
    def eat(self, food):
        print(f"{self.name} is eating {food}")


student_one = Student("Wison", 30, 1)
print(student_one.name, student_one.age, student_one.student_id)  # Wison 30 1
# 使用父類別方法
student_one.sleep()  # Wison is sleeping ...
# 使用子類別方法 <-- 覆寫過的父類別方法
student_one.eat("noodle")  # Wison is eating noodle
