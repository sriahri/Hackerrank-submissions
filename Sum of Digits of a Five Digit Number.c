#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n,sum=0,rem;
    scanf("%d", &n);
    while(n!=0)
    {
      rem=n%10;
        n=n/10;
        sum=sum+rem;
    }
    printf("%d",sum);    //Complete the code to calculate the sum of the five digits on n.
    return 0;
}