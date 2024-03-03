# 應用 User_Inputs
import random

password = random.randint(1, 100)  # 隨機產生位於 1 ~ 100 之間的整數
while True:
    user_input = input("請猜數字: ")
    if int(user_input) == password:
        print("答對了")
        break
    elif int(user_input) > password:
        print("比", user_input, "小")
    elif int(user_input) < password:
        print("比", user_input, "大")
    else:
        print("請輸入數字!")
