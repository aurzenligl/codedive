#include "foo.hpp"
#include <cstdio>
#include <cstdlib>
#include <vector>

/// basics

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

/// vector'esque class

struct IntVec : public std::vector<int>
{
    explicit IntVec(size_t size): std::vector<int>(size)
    { }
};

void* operator new(std::size_t sz)
{
    std::printf("global op new called, size = %zu\n",sz);
    return std::malloc(sz);
}

void operator delete(void* ptr)
{
    std::puts("global op delete called");
    std::free(ptr);
}

IntVec* IntVec_create(size_t size)
{
    return new IntVec(size);
}

void IntVec_delete(IntVec* v)
{
    delete v;
}

int* IntVec_begin(IntVec* v);
size_t IntVec_size(IntVec* v);
void IntVec_push_back(IntVec* v, int x);
void IntVec_resize(IntVec* v, size_t size);
