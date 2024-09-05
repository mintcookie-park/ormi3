import sys
from collections import deque

n = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
list_c = list(map(int, sys.stdin.readline().split()))

res = deque()

for qs in range(n):
    if list_a[qs] == 0:
        res.appendleft(list_b[qs])
        
for i in range(m):
    res.append(list_c[i])
    print(res.popleft(), end=' ')