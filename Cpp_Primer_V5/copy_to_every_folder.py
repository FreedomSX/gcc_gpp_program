import os

# 获取项目文件夹中所有项目文件夹列表
folder_lst = [i for i in os.listdir(".\\") if os.path.isdir(os.path.join(".\\", i))]
# print(folder_lst)

for folder in folder_lst:
    print(folder.find("Environment"))
    if folder.find("Environment") == -1:
        cmdStr = "xcopy .\\Environment .\\" + folder + " /d /y /i /h /e"
        print(cmdStr)
        os.system(cmdStr)
