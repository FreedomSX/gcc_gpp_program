#include <iostream>
#include <ctime>

using namespace std;

extern int max(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    return b;
}

int main()
{
    // long long startTime, endTime;
    // startTime = time(nullptr);
    // cout << startTime << endl;
    // int m = 3, n = 2;
    // for (long long i = 0; i < 18888888888LL; i++)
    {
        m = max(m, n);
    }
    endTime = time(nullptr);
    cout << endTime << endl;
    cout << endTime - startTime << endl;
    return 0;
}