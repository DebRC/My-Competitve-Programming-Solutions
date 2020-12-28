#include <iostream>
using namespace std;

int main() {
    int a,b,c;
    int t;
    cin>>t;
    while(t>0)
    {
        t-=1;
        cin>>a>>b>>c;
        if((a>b and a<c) or (a>c and a<b))
        {
            cout<<a;
        }
        else if((b>a and b<c) or (b>c and b<a))
        {
            cout<<b;
        }
        if((c>b and c<a) or (c>a and c<b))
        {
            cout<<c;
        }
        cout<<"\n";
    }
	// your code goes here
	return 0;
}
