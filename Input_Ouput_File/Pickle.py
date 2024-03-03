import pickle

x = 10
y = [1, 2, 3, 4]

# wb --> write binary --> 生成二進位檔案
with open('.\Input_Ouput_File\pickle_file', 'wb') as p_file:
    # 資料儲存
    pickle.dump(x, p_file)
    pickle.dump(y, p_file)

# rb --> read binary --> 讀取二進位檔案
with open('.\Input_Ouput_File\pickle_file', 'rb') as p_file:
    # 資料讀取
    print(pickle.load(p_file))
    print(pickle.load(p_file))
