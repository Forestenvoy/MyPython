import pickle

x = 10
y = 100
myList = [1, 2, 3, 4, 5, 9]


def save_data():
    # 資料儲存成 二進位檔案
    global x, y, myList
    data = {"x": x, "y": y, "myList": myList}

    with open('.\Input_Ouput_File\pickle_file2', 'wb') as p_file:
        pickle.dump(data, p_file)


save_data()

x = None
y = None
myList = None


def restore_data():
    # 二進位檔案讀取 資料
    global x, y, myList
    with open('.\Input_Ouput_File\pickle_file2', 'rb') as p_file:
        data = pickle.load(p_file)

        x = data['x']
        y = data['y']
        myList = data['myList']


restore_data()

print(x)
print(y)
print(myList)
