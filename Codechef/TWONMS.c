#include <stdio.h>
 
int main(void) {
	// your code goes here
    int t,i;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        long long int a,b,n,c,j,c1=0,c2=0;
        scanf("%Ld %Ld %Ld",&a,&b,&n);
       if(n%2==0)
       {
            if(a>b)
              c=a/b;
            else
              c=b/a;
            printf("%Ld\n",c);
       }
       else
       {
            a=a*2;
           // printf("%Ld ",a);
            if(a>b)
              c=a/b;
            else
              c=b/a;
            printf("%Ld\n",c);
           
       }
       // printf("%Ld %Ld ",a,b);
     
    }
	return 0;
}