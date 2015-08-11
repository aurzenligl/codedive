template <class T>
class First {};

struct MissingSemicolon {}

First<int> first;

template <class T>
void fun(T::type) { }

struct Second { };

void gun()
{
    Second x;
    function<Second>(x);
}
