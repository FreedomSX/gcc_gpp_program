#include <iostream>


using namespace std;

int main()
{
    size_t a = -5;
    int b = 2;
    cout << a+b << endl;
    cout << (a | b) << endl;
    cout << (int)(a | b) << endl;
    char c = 'a';
    cout << (size_t)(a | c) << endl;
    return 0;
}