#include <iostream>
using namespace std;

int main() {
    int n,res;
    cin>>n;
    if(n%4==0)
    {
        res=n+1;
        cout<<res;
    }
    else
    {
        res=n-1;
        cout<<res;
    }
	// your code goes here
	return 0;
}
