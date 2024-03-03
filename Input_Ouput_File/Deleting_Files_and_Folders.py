import os

folder_path = ".\Input_Ouput_File\OsTest"
file_name = "myosTest.txt"
file_path = os.path.join(folder_path, file_name)

# 創建資料夾
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created successfully.")
else:
    print(f"Folder '{folder_path}' already exists.")

# 創建檔案
with open(file_path, "w") as file:
    file.write("This is a sample file content.")
    print(f"File '{file_path}' created successfully.")

# 刪除檔案
os.remove(file_path)
print(f"File '{file_path}' deleted successfully.")


# os.walk() 可以遍歷資料夾內的所有檔案
# 刪除"空"資料夾
os.rmdir(folder_path)
print(f"Folder '{folder_path}' deleted successfully.")
