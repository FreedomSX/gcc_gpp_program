import os

project_name = input("请输入工程名：")
cmd_str = "md " + project_name
os.system(cmd_str)

cmd_str = "xcopy .\\Environment .\\" + project_name + " /d /y /i /h /e"
os.system(cmd_str)

cmd_str = "if not exist main.cpp (echo .>main.cpp)"
os.system(cmd_str)

with open(".\\" + project_name + "\\Codes\\main.cpp", "w", encoding="utf-8") as f:
    str = """
#include <iostream>

using namespace std;

int main()
{
    return 0;
}
    
    """
    f.write(str)