#include <bits/stdc++.h>
#define all(x) begin(x), end(x)
using namespace std;
using ll = long long;

int n, p, d;
int x[17], y[17];
int dp[3000007];

int main(){
    cin.tie(0) -> sync_with_stdio(0);

    cin >> n;
    for(int i=1; i<=n; i++) cin >> x[i] >> y[i];
    cin >> p >> d;
    int pmx = 1 << (n+n);
    for(int mask=1; mask<pmx; mask++) dp[mask] = 1e9;
    for(int i=1; i<=n; i++){
        for(int j=i+1; j<=n; j++){
            int k = abs(x[i] - x[j]) + abs(y[i] - y[j]);
            if(k < d) continue;
            int x = i-1, y = j-1;
            for(int mask=pmx-1; mask>=0; mask--){
                if((mask>>(x+x)&3) == p || (mask>>(y+y)&3) == p) continue;
                int nmask = mask + (1 << (x+x)) + (1 << (y+y));
                dp[nmask] = min(dp[nmask], dp[mask] + k);
            }
        }
    }
    int flow = 0, cost = 2e9;
    for(int mask=0; mask<pmx; mask++){
        if(dp[mask] == 1e9) continue;
        int popcnt = 0;
        for(int i=0; i<n; i++) popcnt += mask >> (i+i) & 3;
        if(popcnt&1 || flow > popcnt/2) continue;
        if(flow == popcnt/2) cost = min(cost, dp[mask]);
        else flow = popcnt/2, cost = dp[mask];
    }
    cout << flow << ' ' << cost;
}