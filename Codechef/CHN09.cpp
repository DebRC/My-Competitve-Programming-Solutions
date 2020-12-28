#include <iostream>
#include<cstring>
using namespace std;

int main() 
{
    int t;
    cin>>t;
    while(t>0){
    char s[100];
    int n, counta=0,countb=0,res;
    cin>>s;
    n=strlen(s);
    for(int i=0;i<n;i++){
    if(s[i]=='a')
    {
        counta+=1;
    }
    else
    {
        countb+=1;
    }}
    if(counta>=countb)
    {
        res=abs(n-counta);
    }
    else
    {
        res=abs(n-countb);
    }
    cout<<res<<"\n";
    t--;
    }
	return 0;
}
