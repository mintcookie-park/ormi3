import sys
input = sys.stdin.readline
from collections import *
dy = [1,-1,0,0,1,1,-1,-1]; dx = [0,0,1,-1,1,-1,1,-1]

def DFS(ocean):
  island = set(); h = 0
  for y,x in ocean:
    if not visited[y][x]:
      island |= BFS(y,x,4,0)
  for y,x in island:
    if not visited[y][x]:
      h = max(h,DFS(BFS(y,x,8,1))+1)
  if len(result)==h:
    result.append(0)
  result[h] += 1
  return h

def BFS(y,x,d,n):
  dq = deque([(y,x)]); S = set()
  while dq:
    y,x = dq.popleft()
    if visited[y][x]:
      continue
    visited[y][x] = 1
    for i in range(d):
      y1,x1 = y+dy[i],x+dx[i]
      if N>y1>=0 and M>x1>=0 and not visited[y1][x1]:
        if board[y1][x1]==n:
          dq.append((y1,x1))
        else:
          S.add((y1,x1))
  return S
        
N,M = map(int,input().split())
M += 2
board = [[0]*M]+[[0]+[*map(lambda x:1 if x=="x" else 0,input().strip())]+[0] for i in range(N)]+[[0]*M]
N += 2

result = []; visited = [[0]*M for i in range(N)]
DFS([(0,0)]); result.pop()
print(*result if result else [-1])