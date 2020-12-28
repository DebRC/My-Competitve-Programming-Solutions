#include <stdio.h>
#include<bits/stdc++.h>
#include<algorithm> 
using namespace std;

int main(void) {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	    {   
	        int r,c,k;
	        cin>>r>>c>>k;
	        int a,b;
	        a=min(c+k,8)- max(c-k,1)+1 ;
	        b=min(r+k,8)-max(r-k,1)+1 ;
	        int ans=(a)*(b);
	        cout<<ans<<"\n";
	    }
	return 0;
}