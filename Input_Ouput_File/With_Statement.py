with open(".\Input_Ouput_File\myFile.txt", "r") as file:
    all_content = file.read()
    print(all_content)
    # Hello, how are you today?
    # I'm fine, thank you.

# with 區塊結束 會自動關閉檔案

# Open()
# mode = "r" 是預設值
with open(".\Input_Ouput_File\myFile.txt") as file:
    print(file.read())
# append mode 新增
with open(".\Input_Ouput_File\myFile.txt", mode="a") as file:
    myString = "Learning python is so fun."
    file.write(myString)
    # Hello, how are you today?
    # I'm fine, thank you.
    # Learning python is so fun.
# Write mode 覆寫
with open(".\Input_Ouput_File\myFile.txt", mode="w") as file:
    myString = "Learning python is so fun."
    file.write(myString)
    # Learning python is so fun.
