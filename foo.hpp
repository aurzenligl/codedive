#ifndef FOO_X
#define FOO_X

#include <stddef.h>

#define LIBLINKAGE __attribute__ ((visibility ("default")))

#ifdef __cplusplus
extern "C" {
#endif

LIBLINKAGE int calls();
LIBLINKAGE extern int X;
LIBLINKAGE int foo(int x);
LIBLINKAGE void bar(int* y);

struct IntVec;
LIBLINKAGE IntVec* IntVec_create(size_t size);
LIBLINKAGE void IntVec_delete(IntVec* v);
LIBLINKAGE int* IntVec_begin(IntVec* v);
LIBLINKAGE size_t IntVec_size(IntVec* v);
LIBLINKAGE void IntVec_push_back(IntVec* v, int x);
LIBLINKAGE void IntVec_resize(IntVec* v, size_t size);

#ifdef __cplusplus
}
#endif

#endif /* FOO_X */
