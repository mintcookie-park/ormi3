#include <bits/stdc++.h>
#define X first
#define Y second
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define ini(x, y) memset(x, y, sizeof(x))
#define endl '\n'
#define fastio cin.sync_with_stdio(false); cin.tie(nullptr)
using namespace std;
 
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
const int MOD = 1e9 + 7;
const int dx[] = { -1, 0, 1, 0, -1, 1, 1, -1 };
const int dy[] = { 0, 1, 0, -1, 1, 1, -1, -1 };
 
struct Dinic {
	struct Edge {
		int to, c, f, r;
		Edge() : Edge(-1, 0, -1) {}
		Edge(int to, int c, int r) : to(to), c(c), f(0), r(r) {}
 
		int spare() {
			return c - f;
		}
	};
 
	vector<vector<Edge>> adj;
	vector<int> depth, work;
 
	bool bfs(int S, int E) {
		fill(all(depth), -1);
 
		queue<int> Q;
		Q.push(S);
		depth[S] = 0;
 
		while (!Q.empty()) {
			int now = Q.front(); Q.pop();
			for (auto &e : adj[now]) {
				if (e.spare() > 0 && depth[e.to] == -1) {
					depth[e.to] = depth[now] + 1;
					Q.push(e.to);
				}
			}
		}
 
		return depth[E] != -1;
	}
	int dfs(int now, int dst, int flow) {
		if (now == dst) return flow;
 
		for (int &i = work[now]; i < sz(adj[now]); ++i) {
			auto &e = adj[now][i];
			if (depth[e.to] == depth[now] + 1 && e.spare() > 0) {
				int f = dfs(e.to, dst, min(flow, e.spare()));
				if (f > 0) {
					e.f += f;
					adj[e.to][e.r].f -= f;
					return f;
				}
			}
		}
 
		return 0;
	}
 
	Dinic(int n) {
		adj.resize(n);
		depth.resize(n);
		work.resize(n);
	}
	void add_edge(int u, int v, int cap) {
		adj[u].emplace_back(v, cap, sz(adj[v]));
		adj[v].emplace_back(u, 0, sz(adj[u]) - 1);
	}
	int max_flow(int S, int E) {
		int flow = 0;
		while (bfs(S, E)) {
			fill(all(work), 0);
			while (1) {
				int f = dfs(S, E, 0x3f3f3f3f);
				if (f == 0) break;
				flow += f;
			}
		}
		return flow;
	}
};
int main() {
	fastio;
	int N, M;
	cin >> N >> M;
 
	int S = 2 * N * M, E = S + 1;
	Dinic dinic(E + 1);
 
	char bo[50][51];
	for (int i = 0; i < N; ++i) {
		cin >> bo[i];
	}
 
	int cost[26];
	for (int i = 0; i < 26; ++i) {
		cin >> cost[i];
	}
 
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			int a = i * M + j << 1, b = a + 1;
 
			if (bo[i][j] == '*') {
				dinic.add_edge(a, b, 0x3f3f3f3f);
				dinic.add_edge(b, E, 0x3f3f3f3f);
			}
			else if (bo[i][j] != '-') {
				dinic.add_edge(a, b, cost[bo[i][j] - 65] + 100000000);
				for (int k = 0; k < 4; ++k) {
					int nx = i + dx[k];
					int ny = j + dy[k];
					if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
					if (bo[nx][ny] == '-') continue;
 
					int aa = nx * M + ny << 1, bb = aa + 1;
					dinic.add_edge(b, aa, 0x3f3f3f3f);
					if (bo[nx][ny] != '*') dinic.add_edge(bb, a, 0x3f3f3f3f);
				}
				if (i % (N - 1) == 0 || j % (M - 1) == 0) {
					dinic.add_edge(S, a, 0x3f3f3f3f);
				}
			}
		}
	}
 
	cout << dinic.max_flow(S, E) % 100000000;
 
	return 0;
}