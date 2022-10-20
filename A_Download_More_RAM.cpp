#include<bits/stdc++.h>
#include<vector>
#include <algorithm>
#define ll long long
#define lld long double
#define lli long long int 
#define sza(x) ((int)x.size())
#define all(a) (a).begin(),(a).end()
#define vll vector<long long int>
#define pb push_back
#define mp make_pair
#define se second
#define fi first

using namespace std;
bool compare(ll a , ll b)
{
if(a>b) return true;
return false;
}
void solve() {
    ll n,k;
   vector<pair<ll ,ll>> ram;
      cin>>n>>k;
      ll a[n] , b[n];
      for(ll i=0; i<n;i++){
          cin>>a[i];
      }
      for(ll i=0; i<n;i++){
          cin>>b[i];
      }
      for(ll i=0; i<n;i++){
          ram.pb(mp(a[i] , b[i]));
      }
      sort(all(ram));
      for(ll i=0; i<n; i++){
          if(ram[i].first <= k){
              k+= ram[i].second;
          }
          else{
              break;
          }
      }
      cout<<k<<endl;
      
  }
int main() {
ios_base::sync_with_stdio(false);
int t=1;
cin>>t;
for( int k=1;k<=t;k++){
solve();
}
return 0;
}