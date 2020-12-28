#include <stdio.h>

int gcd(a, b){

	if(b == 0){
		return a;
	}else{
		return gcd(b, a % b);
	}
}

int main(){

	int T, length, breadth, square_side;

	scanf("%d", &T);

	while(T--){
		scanf("%d%d", &length, &breadth);
		square_side = gcd(length, breadth);
		printf("%d\n", length * breadth/ square_side/ square_side);
	}
	return 0;
}
