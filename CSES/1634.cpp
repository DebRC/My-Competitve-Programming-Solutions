#include<bits/stdc++.h>
using namespace std;
#define ll long long
 
ll change(ll *coins, ll n,ll bal)
{
    ll dp[bal+1] {0};
    for(ll i=1;i<=bal;i++)
    {
        dp[i]=(bal+1);
    }
    // for(ll i=0;i<=bal;i++)
    // {
    //     cout<<dp[i]<<" ";
    // }
    // cout<<endl;
    for(ll i=1;i<=bal;i++)
    {
        for(ll j=0;j<n;j++)
        {
            if (coins[j]<=i)
                {
                    ll op1=dp[i];
                    ll op2=1+dp[i-coins[j]];
                    dp[i]=min(op1,op2);
                }
        }
    }
    // for(ll i=0;i<=bal;i++)
    // {
    //     cout<<dp[i]<<" ";
    // }
    // cout<<endl;
    if (dp[bal]>bal)
    return -1;
    return dp[bal];
}
 
int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    srand(chrono::high_resolution_clock::now().time_since_epoch().count());
    ll n,bal;
    cin>>n>>bal;
    ll x[n];
    for(ll i=0;i<n;i++)
    {
        cin>>x[i];
    }
    // for(ll i=0;i<n;i++)
    // {
    //     cout<<x[i]<<" ";
    // }
    // cout<<endl;
    cout<<change(x,n,bal);
    return 0;
}