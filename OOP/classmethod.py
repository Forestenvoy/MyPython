class Circle:
    """ This class creates circles """
    pi = 3.1415926
    all_circles = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)

    # 圓的面積
    def area(self):
        return self.__class__.pi * (self.radius ** 2)

    # 靜態方法 不須實體化即可呼叫
    @staticmethod
    def total_area():  # cls --> stand for class 引用類別本身
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total

    # 類別方法 也不須實體化即可呼叫
    @classmethod
    def total_area2(cls):  # cls --> stand for class 引用類別本身
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total


c1 = Circle(10)
c2 = Circle(15)

print(c1.area())
print(c2.area())

print(Circle.total_area())
print(Circle.total_area2())
