import sys
V, E = map(int, input().split())
INF = 10000 * V + 1 #전체 사이클을 돌 경우 최댓값 +1
distance = [[INF for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    start, end, dist = map(int, sys.stdin.readline().split())
    distance[start][end] = dist

#플로이드 워셜 알고리즘
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            distance[i][j] = min(distance[i][j],
                                 distance[i][k] + distance[k][j])

#가장 작은 사이클 찾는 for문
min_cycle = INF
for i in range(1, V+1):
    min_cycle = min(min_cycle, distance[i][i])
    
if min_cycle == 10000 * V + 1: #사이클이 없을 경우
    print(-1)
else:
    print(min_cycle)