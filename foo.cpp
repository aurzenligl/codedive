#include "foo.hpp"

int calls()
{
    static int calls = 0;
    return calls++;
}

int X = 2;

int foo(int x)
{
    return x * X;
}

void bar(int* y)
{
    *y = 42;
}
