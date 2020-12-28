#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
#define ll long long
#define M 1000000007
#define sz(a) (ll)a.size()
#define pll pair<ll,ll>
#define rep(i,a,b) for(ll i=(ll)a;i<(ll)b;i++)
#define sep(i,a,b) for(ll i=(ll)a;i>=(ll)b;i--)
#define mll map<ll,ll>
#define vl vector<ll>
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define all(a) a.begin(),a.end()
#define F first
#define S second
using namespace __gnu_pbds;
using namespace std;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
ll f(ll p,ll q)
{
	return p/q+1;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    ll t,p,q,n;
    cin>>t;
    while(t--)
    {
    	cin>>p>>q>>n;
    	//if((2*abs(p-q))%q==0)
    		cout<<f((n-1)*q,2*abs(p-q))<<"\n";
    	//else if(((n-1)*q)%(2*abs(p-q))==0)
    	//	cout<<(n-1)*q/(2*abs(p-q))+1<<"\n";  
    	//else
    	//	cout<<f(n*q,2*abs(p-q))<<"\n";
    }
}
