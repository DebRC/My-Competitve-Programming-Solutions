#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
template <class T> using Tree = tree<T, null_type, less<T>, rb_tree_tag,tree_order_statistics_node_update>;
 
#define FOR(i, a, b) for (int i=a; i<(b); i++)
#define F0R(i, a) for (int i=0; i<(a); i++)
#define FORd(i,a,b) for (int i = (b)-1; i >= a; i--)
#define F0Rd(i,a) for (int i = (a)-1; i >= 0; i--)
 
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound
#define all(x) x.begin(), x.end()
 
const int MOD = 1000000007;
 
int n,x,h[1000],s[1000], bes[100001];
 
int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    cin >> n >> x;
    F0R(i,n) cin >> h[i];
    F0R(i,n) cin >> s[i];
    F0R(i,n) F0Rd(j,x-h[i]+1) bes[j+h[i]] = max(bes[j+h[i]],bes[j]+s[i]);
    cout << bes[x];
}