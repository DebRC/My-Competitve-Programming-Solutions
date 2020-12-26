#include <bits/stdc++.h> 
using namespace std; 
 
long long maxVal(long long x, long long y) { return (x >= y)? x: y; } 
 
long long constructSTUtil(long long arr[], long long ss, long long se, long long *st, long long si)  
{ 
    if (ss == se)  
    {  
        st[si] = arr[ss];  
        return arr[ss];  
    }
    long long mid=ss+(se-ss)/2; 
    st[si] = maxVal(constructSTUtil(arr, ss, mid, st, si*2+1),constructSTUtil(arr, mid+1, se, st, si*2+2));  
    return st[si];  
}
 
long long *constructST(long long arr[], long long n)  
{
    long long *st = new long long[4*n];
    constructSTUtil(arr, 0, n-1, st, 0);
    return st;  
}
 
long long get(long long *st,long long q,long long si,long long ss,long long se)
{
    if(q>st[si])
        return -1;
    if(ss==se)
        return ss;
    long long mid=ss+(se-ss)/2;
    if(st[2*si+1]>=q)
        return get(st,q,2*si+1,ss,mid);
    else
        return get(st,q,2*si+2,mid+1,se);
}
 
void updateValue(long long *h,long long *st,long long ss,long long se,long long i,long long value,long long si)
{
    if (ss==se)
    {
        st[si]=value;
        h[i]=value;
    }
    else
    {
        long long mid=ss+(se-ss)/2;
        if (i>=ss and i<=mid)
        {
            updateValue(h,st,ss,mid,i,value,2*si+1);
        }
        else
        {
            updateValue(h,st,mid+1,se,i,value,2*si+2);
        }
        st[si]=maxVal(st[2*si+1],st[2*si+2]);
    }
}
 
int main()  
{  
    long long n,m;
    cin>>n>>m;
    long long h[n];
    for(long long i=0;i<n;i++)
    {
        cin>>h[i];
    }
    long long *st = constructST(h,n);
    long long g[m];
    for(long long i=0;i<m;i++)
    {
        cin>>g[i];
        long long room=get(st,g[i],0,0,n-1);
        if (room==-1){cout<<0<<" ";}
        else
        {
            updateValue(h,st,0,n-1,room,h[room]-g[i],0);
            cout<<room+1<<" ";
        }
    }
    return 0;
}