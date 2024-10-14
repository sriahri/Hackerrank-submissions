#include <stdio.h>
#include<math.h>
void update(int *,int *);

void update(int *x,int *y) {
    int a1=(*x)+(*y);
    int b1=(abs((*x)-(*y)));
     printf("%d\n%d", a1, b1);

}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    return 0;
}