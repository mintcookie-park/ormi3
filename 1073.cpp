#include<bits/stdc++.h>
#define FOR(i, j, k) for(int i = j; i<=k; i++)
using namespace std;

using ll = long long;

int deg[10];
int dp[10];
int main(void) {
	ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
	int N; cin >> N;
	FOR(i, 1, N) {
		int a; cin >> a;
		deg[a / 10]++;
		deg[a % 10]++;
	}
	dp[0] = 1;
	for (int i = 2; i <= 8; i += 2) {
		dp[i] = (i - 1)*dp[i - 2];
	}
	ll ans = 1;
	for (int i = 0; i <= 9; i++) {
		ans *= dp[deg[i]];
	}
	cout << ans;
}