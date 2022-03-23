#include <cstdio>

int main()
{
    int a = -5;
    printf("%x\n", a);
    printf("%x\n", (unsigned char)(a));
    int b;
    b = a << 1;
    printf("%d ", b);
    printf("%x \n", b);
    printf("%x\n", (unsigned char)(a) << 1);
    getchar();
    return 0;
}