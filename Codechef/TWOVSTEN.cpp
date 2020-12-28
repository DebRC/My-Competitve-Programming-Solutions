#include <iostream>
using namespace std;

int main() {
    int n=0,t=0,count;
    cin>>t;
    while(t>0)
    {
        count=0;
        cin>>n;
        if(n%5!=0)
        {
            cout<<"-1";
        }
        else
        {
            while(1)
            {
                if(n%10!=0)
                {
                    n=2*n;
                    count+=1;
                }
                else
                {
                    break;
                }
            }
            cout<<count;
        }
        cout<<"\n";
        t-=1;
    }
	// your code goes here
	return 0;
}