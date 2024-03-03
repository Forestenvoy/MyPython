# I/O with File for Python

# 1. file = open(file_name, mode)
# open 函數的文件路徑是相對路徑時，Python 會根據工作區(非原始檔位置)來解析相對路徑。 <-- 看你終端機執行位置解析相對路徑
file = open(".\Input_Ouput_File\myFile.txt", "r")
print(file)
# <_io.TextIOWrapper name='myFile.txt' mode='r' encoding='cp950'>

print(file.read())
# Hello, how are you today?
# I'm fine, thank you.
# 同時文件指針會指向檔案資料的末端

file.seek(0)  # 重新設置文件指針
print(file.read(5))
# Hello

file.seek(0)
print(type(file.read()))
# <class 'str'> --> read() 回傳的是字串
