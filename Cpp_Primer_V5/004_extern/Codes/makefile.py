import os


os.system("del *.o -f")

file_lst = []
main_file = ""
for file in os.listdir(".\\"):
    if file.endswith(".cpp"):
        file_lst.append(file)

for num, file in enumerate(file_lst):
    print(num, file)
main_file_num = int(input("请输入包含main文件编号："))

file_name_lst = ""
file_name_temp = ""
link_cmd_str = ""
for file in file_lst:
    file_name_temp = file.split(".")[0]
    print(file, "is compiling...")
    link_cmd_str += file_name_temp + ".o "
    cmdStr = "g++ -c " + file + " -o " + file_name_temp + ".o"
    os.system(cmdStr)
    print(file, "is compilied!")

link_cmd_str = "g++ " + link_cmd_str + " -o " + file_lst[main_file_num].split(".")[0]
print(link_cmd_str)
os.system(link_cmd_str)

print("Complied!")

