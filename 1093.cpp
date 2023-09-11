#include<cstdio>
#include<algorithm>
using namespace std;
int n, m, v[32], c[32], k, s, cnt[2] = { 1,1 }, r = 1e9;
pair<int, int> p[2][1 << 16];
int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", c + i);
    for (int i = 0; i < n; i++) scanf("%d", v + i);
    scanf("%d%d", &k, &m);
    for (int i = 0, x; i < m; i++) {
        scanf("%d", &x);
        s += c[x];
    }
    for (int i = 0; i < n; i++) {
        int h = i >= n / 2;
        for (int j = 0; j < cnt[h]; j++) p[h][j + cnt[h]] = { p[h][j].first + v[i],p[h][j].second + c[i] };
        cnt[h] *= 2;
    }
    sort(p[1], p[1] + cnt[1]);
    for (int j = cnt[1] - 1; j--;) p[1][j].second = min(p[1][j].second, p[1][j + 1].second);
    for (int i = 0; i < cnt[0]; i++) {
        int lb = lower_bound(p[1], p[1] + cnt[1], make_pair(k - p[0][i].first, 0)) - p[1];
        if (lb < cnt[1]) r = min(r, p[0][i].second + p[1][lb].second);
    }
    printf("%d", r < 1e9 ? max(r - s, 0) : -1);
    return 0;
}