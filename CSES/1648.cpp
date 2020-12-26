#include <bits/stdc++.h> 
using namespace std; 
 
//long long minVal(long long x, long long y) { return (x < y)? x: y; } 
 
long long getMid(long long s, long long e) { return s + (e -s)/2; }  
 
long long getSumUtil(long long *st, long long ss, long long se, long long qs, long long qe, long long si)  
{  
    if (qs <= ss && qe >= se)  
        return st[si];
    if (se < qs || ss > qe)  
        return 0;
    long long mid = getMid(ss, se);  
    return (getSumUtil(st, ss, mid, qs, qe, 2*si+1)+getSumUtil(st, mid+1, se, qs, qe, 2*si+2));  
}  
 
long long getSum(long long *st, long long n, long long qs, long long qe)  
{
    return getSumUtil(st, 0, n-1, qs, qe, 0);  
}  
 
long long constructSTUtil(long long arr[], long long ss, long long se, long long *st, long long si)  
{ 
    if (ss == se)  
    {  
        st[si] = arr[ss];  
        return arr[ss];  
    }
    long long mid = getMid(ss, se);  
    st[si] = (constructSTUtil(arr, ss, mid, st, si*2+1)+constructSTUtil(arr, mid+1, se, st, si*2+2));  
    return st[si];  
}
 
long long *constructST(long long arr[], long long n)  
{
    long long x = (long long)(ceil(log2(n)));
    long long max_size = 2*(long long)pow(2, x) - 1;
    long long *st = new long long[max_size];
    constructSTUtil(arr, 0, n-1, st, 0);
    return st;  
}  
 
void updateValueUtil(long long *st, long long ss, long long se, long long i, long long diff, long long si)  
{
    if (i < ss || i > se)  
        return;
    st[si] = st[si] + diff;  
    if (se != ss)  
    {  
        long long mid = getMid(ss, se);  
        updateValueUtil(st, ss, mid, i, diff, 2*si + 1);  
        updateValueUtil(st, mid+1, se, i, diff, 2*si + 2);  
    }  
}  
 
void updateValue(long long arr[], long long *st, long long n, long long i, long long new_val)  
{ 
    long long diff = new_val - arr[i];
    arr[i] = new_val;
    updateValueUtil(st, 0, n-1, i, diff, 0);  
}  
 
int main()  
{  
    long long n,q,a,b,c;
    cin>>n>>q;
    long long arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    long long *st = constructST(arr, n);
    while(q>0)
    {
        q--;
        cin>>c>>a>>b;
        if(c==1){ updateValue(arr,st,n,a-1,b);}
        else {
        cout<<getSum(st, n, a-1, b-1)<<endl;}
    }
    return 0;  
} 