#include <bits/stdc++.h> 
using namespace std;
#define MAX 1000000
 
long long tree[MAX] = {0};
long long lazy[MAX] = {0};
 
void updateRangeUtil(long long si, long long ss, long long se, long long us, long long ue, long long diff) 
{ 
    if (lazy[si] != 0) 
    {
        tree[si] += (se-ss+1)*lazy[si];
        if (ss != se) 
        {
            lazy[si*2 + 1]+= lazy[si]; 
            lazy[si*2 + 2]+= lazy[si]; 
        }
        lazy[si] = 0; 
    }
    if (ss>se || ss>ue || se<us) 
        return ;
    if (ss>=us && se<=ue) 
    { 
        tree[si] += (se-ss+1)*diff;
        if (ss != se) 
        {
            lazy[si*2 + 1]   += diff;
            lazy[si*2 + 2]   += diff;
        }
        return;
    }
    long long mid = (ss+se)/2; 
    updateRangeUtil(si*2+1, ss, mid, us, ue, diff); 
    updateRangeUtil(si*2+2, mid+1, se, us, ue, diff);
    tree[si] = tree[si*2+1] + tree[si*2+2]; 
}
 
void updateRange(long long n, long long us, long long ue, long long diff) 
{ 
   updateRangeUtil(0, 0, n-1, us, ue, diff); 
} 
  
 
long long getSumUtil(long long ss, long long se, long long qs, long long qe, long long si) 
{ 
    if (lazy[si] != 0) 
    { 
        tree[si] += (se-ss+1)*lazy[si]; 
        if (ss != se) 
        { 
            lazy[si*2+1] += lazy[si]; 
            lazy[si*2+2] += lazy[si]; 
        } 
        lazy[si] = 0; 
    } 
    if (ss>se || ss>qe || se<qs) 
        return 0;
    if (ss>=qs && se<=qe) 
        return tree[si];
    long long mid = (ss + se)/2; 
    return getSumUtil(ss, mid, qs, qe, 2*si+1) + getSumUtil(mid+1, se, qs, qe, 2*si+2); 
} 
 
long long getSum(long long n, long long qs, long long qe) 
{
    return getSumUtil(0, n-1, qs, qe, 0); 
} 
  
 
void constructSTUtil(long long arr[], long long ss, long long se, long long si) 
{
    if (ss > se) 
        return;
    if (ss == se) 
    { 
        tree[si] = arr[ss]; 
        return; 
    }
    long long mid = (ss + se)/2;
    constructSTUtil(arr, ss, mid, si*2+1);
    constructSTUtil(arr, mid+1, se, si*2+2);
    tree[si] = tree[si*2 + 1] + tree[si*2 + 2]; 
} 
 
void constructST(long long arr[], long long n) 
{
    constructSTUtil(arr, 0, n-1, 0); 
} 
 
int main()  
{  
    long long n,q,a,b,c,u;
    cin>>n>>q;
    long long arr[n];
    for(long long i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    constructST(arr, n);
    while(q>0)
    {
        q--;
        cin>>c;
        if(c==2)
        {
            cin>>a;
            cout<<getSum(n,a-1,a-1)<<endl;
        }
        else
        {
            cin>>a>>b>>u;
            updateRange(n,a-1,b-1,u);
        }
    }
    return 0;  
}