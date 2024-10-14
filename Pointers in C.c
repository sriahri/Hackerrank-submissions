#include <stdio.h>
#include<math.h>

void update(int *a,int *b) {
    // Complete this funct//
    printf("%d\n",*a+*b);
    printf("%d",abs(*a-*b));
    
    
    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);

    return 0;
}