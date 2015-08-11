#include "foo.hpp"

int X = 2;

int foo(int x)
{
    return x * X;
}

int calls()
{
    static int calls = 0;
    return calls++;
}
