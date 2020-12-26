#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
ll change(ll *coins, ll n,ll bal)
{
    ll dp[bal+1] {0};
    dp[0]=1;
    for(ll i=1;i<=bal;i++)
    {
        for(ll j=0;j<n;j++)
        {
            if (i-coins[j]<0)
                {
                    continue;
                }
            dp[i]=(dp[i]+dp[i-coins[j]])%mod;
        }
    }
    return dp[bal]%mod;
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
    cout<<change(x,n,bal)%mod;
    return 0;
}