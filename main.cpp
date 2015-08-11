#include <stdio.h>
#include "foo.hpp"

int X;

int main()
{
    printf("%d\n", foo(10));
    X = 10;
    printf("%d\n", foo(10));
}
