#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int mod = 1'000'000'007;
ll dp[10000006];
ll dice(ll sum)
{
    if (sum<0) return 0;
    if (sum==0) return 1;
    if (dp[sum]>0) return (dp[sum]%mod);
    if (sum==1) dp[sum]=dice(sum-1);
    else if (sum==2) dp[sum]=dice(sum-1)+dice(sum-2);
    else if (sum==3) dp[sum]=dice(sum-1)+dice(sum-2)+dice(sum-3);
    else if (sum==4) dp[sum]=dice(sum-1)+dice(sum-2)+dice(sum-3)+dice(sum-4);
    else if (sum==5) dp[sum]=dice(sum-1)+dice(sum-2)+dice(sum-3)+dice(sum-4)+dice(sum-5);
    else if (sum>=6) dp[sum]=dice(sum-1)+dice(sum-2)+dice(sum-3)+dice(sum-4)+dice(sum-5)+dice(sum-6);
    return (dp[sum]%mod);
}
 
int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    srand(chrono::high_resolution_clock::now().time_since_epoch().count());
    ll sum;
    cin>>sum;
    cout<<dice(sum);
    return 0;
}