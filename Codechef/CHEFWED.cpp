#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n,k,i,j;
	    cin>>n>>k;
	    int a[n+1];
	    for(i=1;i<=n;i++)
	        cin>>a[i];
	       
	   int c[n+2]; c[n+1]=0;
	   for(i=n;i>=1;i--)
	   {
	       int f[101]={0};
	       int mef=INT_MAX,ef=k;
	       for(j=i;j<=n;j++)
	       {
	           f[a[j]]+=1;
	           if(f[a[j]]==2) ef+=2;
	           else if(f[a[j]]>2) ef+=1;
	           if(mef>ef+c[j+1])
	                mef=ef+c[j+1];
	           
	       }
	       c[i]=mef;
	   }
	   cout<<c[1]<<endl;
	    
    }
	return 0;
}
