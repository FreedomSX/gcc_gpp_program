#include <iostream>
#include <cstdio>

#include <Windows.h>

using namespace std;

int main()
{
    printf("dkfjasd" "kdkfa");
    printf("\n");
    std::cout << "kdfk" "kdkkkkkk" << std::endl;
    float f2 = 5 * .3;
    std::cout << f2 << std::endl;
    float f1 = 2 * 2.;
    std::cout << f1 << std::endl;
    char c3 = '\12';
    std::cout << int(c3) << std::endl;
    char c2 = '\a';
    std::cout << int(c2) << std::endl;
    char c1 = '\n';
    std::cout << int(c1) << std::endl;
    int a = 024;
    std::cout << a << std::endl;
    float f = 3.14159e2;
    std::cout << f << std::endl;
    char c = 'a';
    std::cout << c << std::endl;
    string str = "abc\b";
    std::cout << str << std::endl;
    string str1 = "abc\0612";
    std::cout << str1 << std::endl;
    string str2 = "abc\x21h3";
    std::cout << str2 << std::endl;
    std::cout << '\115' << std::endl;
    std::cout << "kdkf\115" << std::endl;
    // SetConsoleOutputCP(65001);  // 更改cmd编码为utf8
    std::cout << "我是谁" << std::endl;
    std::cout << u"我是谁" << std::endl;
    std::cout << U"我是谁" << std::endl;
    std::cout << L"我是谁" << std::endl;
    std::cout << u8"我是谁" << std::endl;
    return 0;
}