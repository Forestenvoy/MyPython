class C:
    def do_stuff(self):
        print("hello from class C")


class D:
    def do_another_stuff(self):
        print("hello from class D")


class A(C, D):  # 多重繼承
    pass


a = A()  # a 可以使用 C 和 D 的方法
a.do_stuff()  # hello from class C
a.do_another_stuff()  # hello from class D
