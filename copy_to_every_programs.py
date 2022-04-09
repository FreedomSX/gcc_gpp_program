import os

# 获取项目文件夹中所有项目文件夹列表
folder_lst = [i for i in os.listdir(".\\") if os.path.isdir(os.path.join(".\\", i)) and not i.startswith(".") and not i.startswith("Environment")]
print(folder_lst)

for folder in folder_lst:
    print(folder.find("Environment"))
    if folder.find("Environment") == -1:
        cmdStr = "xcopy .\\Environment .\\" + folder + "\\Environment /d /y /i /h /e"
        print(cmdStr)
        os.system(cmdStr)
    cmdStr = "copy .\\copy_to_every_folder.py .\\" + folder + "\\copy_to_every_folder.py /y"
    print(cmdStr)
    os.system(cmdStr)
    cmdStr = "copy .\\del_py_tools.py .\\" + folder + "\\del_py_tools.py /y"
    print(cmdStr)
    os.system(cmdStr)
    cmdStr = "copy .\\new_a_project.py .\\" + folder + "\\new_a_project.py /y"
    print(cmdStr)
    os.system(cmdStr)
    # cmdStr = "rd .\\" + folder + "\\Codes /s /q"
    # print(cmdStr)
    # os.system(cmdStr)
    # cmdStr = "rd .\\" + folder + "\\Environment /s /q"
    # print(cmdStr)
    # os.system(cmdStr)

    #test