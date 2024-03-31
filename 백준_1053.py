from itertools import *

def DFS(start,end,DP):
  for i,j in [(1,0),(0,1),(1,1)]:
    if DP[start+i][end-j]==N:
      DFS(start+i,end-j,DP)
    DP[start][end] = min(DP[start][end],DP[start+i][end-j]+int(not(i and j and seq[start]==seq[end])))

def palin():
  if N==1:
    return 0
  DP = [[N*int(i<j) for j in range(N)] for i in range(N)]
  DFS(0,N-1,DP)
  return DP[0][-1]

seq = [*input()]; N = len(seq)

result = palin()
for i,j in combinations(range(N),2):
  seq[i],seq[j] = seq[j],seq[i]
  result = min(result,palin()+1)
  seq[i],seq[j] = seq[j],seq[i]
print(result)