#include <iostream>
#include <ctime>

using namespace std;

int main()
{
    long long timeStart;
    timeStart = time(NULL);
    long long n = 0;
    cout << "timeStart: " << timeStart << endl;
    volatile long long i;
    for (i = 0; i < 4000000000L; i++)
    {
        n++;
    }
    long long timeEnd;
    timeEnd = time(NULL);
    cout << "timeEnd: " << timeEnd << endl;
    cout << "Duration: " << timeEnd - timeStart << endl;
    return 0;
}