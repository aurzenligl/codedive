#include "foo.hpp"
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

__attribute__((constructor))
void dlentry(void)
{
    std::puts("SO loaded");
}

__attribute__((destructor))
void dlexit(void)
{
    std::puts("SO unloaded");
}

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

template<typename T>
struct Alloc: private std::allocator<T>
{
    typedef std::allocator<T> base_type;
    typedef typename base_type::size_type       size_type;
    typedef typename base_type::difference_type difference_type;
    typedef typename base_type::pointer         pointer;
    typedef typename base_type::const_pointer   const_pointer;
    typedef typename base_type::reference       reference;
    typedef typename base_type::const_reference const_reference;
    typedef typename base_type::value_type      value_type;

    template<typename T1>
    struct rebind
    {
        typedef Alloc<T1> other;
    };

    Alloc() { }

    Alloc(const Alloc& __a): std::allocator<T>(__a) { }

    template<typename T1>
    Alloc(const Alloc<T1>&) { }

    using base_type::construct;
    using base_type::max_size;
    using base_type::destroy;

    pointer allocate(size_type n, const void* = 0)
    {
        std::printf("SO allocate %zu ints\n", n);
        return std::allocator<T>::allocate(n);
    }

    void deallocate(pointer p, size_type)
    {
        std::puts("SO deallocate");
        std::allocator<T>::deallocate(p, 0);
    }
};

struct IntVec : public std::vector<int, Alloc<int> >
{
    explicit IntVec(size_t size): std::vector<int, Alloc<int> >(size)
    { }
};

IntVec* IntVec_create(size_t size)
{
    return new IntVec(size);
}

void IntVec_delete(IntVec* v)
{
    delete v;
}

int* IntVec_begin(IntVec* v)
{
    return v->data();
}

size_t IntVec_size(IntVec* v)
{
    return v->size();
}

void IntVec_push_back(IntVec* v, int x)
{
    v->push_back(x);
}

void IntVec_resize(IntVec* v, size_t size)
{
    v->resize(size);
}

void IntVec_sort(IntVec* v, Comp comp)
{
    std::sort(v->begin(), v->end(), comp);
}
