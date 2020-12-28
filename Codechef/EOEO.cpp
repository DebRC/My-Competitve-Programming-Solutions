#include <iostream>
using namespace std;

int main() 
{
	int t=0;
	cin>>t;
	while(t>0)
	{
	    t-=1;
	    long long int ts=0,js=0;
	    cin>>ts;
	    while(ts%2==0)
	    {
	        ts=ts/2;
	    }
	    js=ts/2;
	    cout<<js<<"\n";
	}
	return 0;
}
