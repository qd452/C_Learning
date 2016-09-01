#include <stdio.h>

#ifdef __GNUC__
int popcount(int x) {
  return __builtin_popcount(x);
}
#else
#error Unimplemented popcount
#endif


int main(void)
{
  int x;
  scanf("%d", &x);

  printf("%d\n", popcount(x));

  return 0;
}