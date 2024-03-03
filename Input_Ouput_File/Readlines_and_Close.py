file = open(".\Input_Ouput_File\myFile.txt", "r")

# readline() 回傳單行字串
print(file.readline())
# Hello, how are you today?
file.seek(0)
# 利用迴圈讀取一筆一筆的資料 <-- 可以避免電腦記憶體被塞滿
while True:
    line = file.readline()
    if line == "":
        break
    else:
        print(line, end="")
# Hello, how are you today?
# I'm fine, thank you.

file.seek(0)
# readlines() 回傳的是 list ，包含每一行的資料 and 換行符號
print(file.readlines())
# ['Hello, how are you today?\n', "I'm fine, thank you.\n"]
file.seek(0)
for line in file.readlines():
    print(line, end="")
# Hello, how are you today?
# I'm fine, thank you.

# 關閉 "檔案 Object"
file.close()
