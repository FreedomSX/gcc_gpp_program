import os

exe_file_lst = [exe_file for exe_file in os.listdir(".\\") if exe_file.endswith(".exe")]

for num, exe_file in enumerate(exe_file_lst):
    print(num, exe_file)

num_of_exe_file  = int(input("请输入exe文件编号："))
print("##############################")

os.system(exe_file_lst[num_of_exe_file])

print("##############################")