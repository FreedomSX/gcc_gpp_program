#include <iostream>

using namespace std;

int main()
{
    int i = 0;
    int &j = i;
    int *k = &i;
    int *&p = k;
    int &*q = k;
    return 0;
}