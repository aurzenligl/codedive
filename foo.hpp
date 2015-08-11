#ifndef FOO_X
#define FOO_X

#define LIBLINKAGE __attribute__ ((visibility ("default")))

#ifdef __cplusplus
extern "C" {
#endif

LIBLINKAGE extern int X;
LIBLINKAGE int foo(int x);
LIBLINKAGE int calls();

#ifdef __cplusplus
}
#endif

#endif /* FOO_X */
