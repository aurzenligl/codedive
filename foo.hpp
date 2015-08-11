#ifndef FOO_X
#define FOO_X

#ifdef __cplusplus
extern "C" {
#endif

__attribute__ ((visibility ("default")))
extern int X;

__attribute__ ((visibility ("default")))
int foo(int x);

__attribute__ ((visibility ("default")))
int calls();

#ifdef __cplusplus
}
#endif

#endif /* FOO_X */
