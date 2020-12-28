#include <stdio.h>
int main()
 {
	double A,B,K;
	char C;
	scanf("%lf %lf %c", &A, &B, &C);
	switch(C)
	{
	    case '+': K = A + B;
	              break;
	    case '-': K = A - B;
	              break;          
	    case '*': K = A * B;
	              break;
	    case '/': K = A / B;
	              break;
	}
	printf("%.7lf\n",K);
	return 0;
}