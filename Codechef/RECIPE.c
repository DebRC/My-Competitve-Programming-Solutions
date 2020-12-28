#include<stdio.h>
int main()
{
	int t,a[50],n,i,c,j,min;
	scanf("%d",&t);
	while(t)
	{
		c=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		scanf("%d",&a[i]);
		min=a[0];
		for(i=1;i<n;i++)
		{
			if(a[i]<min)
			min=a[i];
		}
		for(j=min;j>0;j--)
		{
			for(i=0;i<n;i++)
			{
				if(a[i]%j==0)
				c++;
			}
			if(c==n)
			break;
			c=0;
		}
		for(i=0;i<n;i++)
		printf("%d ",a[i]/j);
		printf("\n");
		t-=1;
	}
	return 0;
}