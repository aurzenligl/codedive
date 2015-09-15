#ifndef FOO_X
#define FOO_X

#include <stddef.h>
#include <stdbool.h>

#define LIBLINKAGE __attribute__ ((visibility ("default")))

#ifdef __cplusplus
extern "C" {
#endif

LIBLINKAGE int calls(void);
LIBLINKAGE extern int X;
LIBLINKAGE int foo(int x);
LIBLINKAGE void bar(int* y);

typedef struct IntVec IntVec;
typedef bool (*Comp)(int a, int b);
LIBLINKAGE IntVec* IntVec_create(size_t size);
LIBLINKAGE void IntVec_delete(IntVec* v);
LIBLINKAGE int* IntVec_begin(IntVec* v);
LIBLINKAGE size_t IntVec_size(IntVec* v);
LIBLINKAGE void IntVec_push_back(IntVec* v, int x);
LIBLINKAGE void IntVec_resize(IntVec* v, size_t size);
LIBLINKAGE void IntVec_sort(IntVec* v, Comp comp);

#ifdef __cplusplus
}
#endif

#endif /* FOO_X */
