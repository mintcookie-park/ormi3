#include <cstdio>

#include <cstring>

#include <vector>

#include <queue>

#include <functional>

#include <utility>



using namespace std;



typedef pair<int, int> P; //노드, 거리



int main(void) {

int V, u, v, w;

vector<P> adj[100001];

bool visited[100001] = { false };

int cost[100001] = { 0 };

queue<int> q;

int curr, next, weight, max_weight=0,max_node;



#ifndef ONLINE_JUDGE

freopen("input.txt", "r", stdin);

freopen("output.txt", "w", stdout);

#endif



scanf("%d\n", &V);

for (int i = 0; i < V; i++) {

scanf("%d", &u);

do

{

scanf("%d", &v);

if (v != -1) {

scanf("%d", &w);

adj[u].push_back(P(v, w));

}



} while (v!=-1);

}



q.push(1); //1번 노드를 기준으로 BFS

while (!q.empty()) {

curr = q.front();

q.pop();

visited[curr] = true;

for (int i = 0; i < adj[curr].size(); i++) {

next = adj[curr][i].first;

if (visited[next] == false) {

weight = adj[curr][i].second;

cost[next] = cost[curr] + weight;

if (cost[next] > max_weight) {

max_weight = cost[next];

max_node = next;

}

q.push(next);

}

}

}



memset(visited, 0, sizeof visited);

memset(cost, 0, sizeof cost);



q.push(max_node); // 위의 BFS수행에서 나온 노드를 바탕으로 한번더 수행

while (!q.empty()) {

curr = q.front();

q.pop();

visited[curr] = true;

for (int i = 0; i < adj[curr].size(); i++) {

next = adj[curr][i].first;

if (visited[next] == false) {

weight = adj[curr][i].second;

cost[next] = cost[curr] + weight;

if (cost[next] > max_weight) {

max_weight = cost[next];

max_node = next;

}

q.push(next);

}

}

}



printf("%d\n", max_weight);





#ifndef ONLINE_JUDGE

fclose(stdin);

fclose(stdout);

#endif



return 0;



}