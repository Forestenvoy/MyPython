
def stars2(n):
    for i in range(1, n+1):
        print("*" * i)
    for i in range(n-1, 0, -1):
        print("*" * i)
    print("-----")


stars2(1)
# *
stars2(2)
# *
# **
# *
stars2(3)
# *
# **
# ***
# **
# *
stars2(4)
# *
# **
# ***
# ****
# ***
# **
# *
