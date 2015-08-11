#ifndef FOO_X
#define FOO_X

#define LIBLINKAGE __attribute__ ((visibility ("default")))

#ifdef __cplusplus
extern "C" {
#endif

LIBLINKAGE int calls();
LIBLINKAGE extern int X;
LIBLINKAGE int foo(int x);
LIBLINKAGE void bar(int* y);

#ifdef __cplusplus
}
#endif

#endif /* FOO_X */
