import sys
from collections import deque

n, t = map(int, sys.stdin.readline().split())
check = [[False] * (n + 1) for _ in range(n + 1)]
signals = [[[]] * (n + 1) for _ in range(n + 1)]
move = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
traffic = {
    1: (move['right'], [move['up'], move['right'], move['down']]),
    2: (move['up'], [move['left'], move['up'], move['right']]),
    3: (move['left'], [move['up'], move['left'], move['down']]),
    4: (move['down'], [move['right'], move['down'], move['left']]),
    5: (move['right'], [move['up'], move['right']]),
    6: (move['up'], [move['left'], move['up']]),
    7: (move['left'], [move['left'], move['down']]),
    8: (move['down'], [move['down'], move['right']]),
    9: (move['right'], [move['right'], move['down']]),
    10: (move['up'], [move['up'], move['right']]),
    11: (move['left'], [move['up'], move['left']]),
    12: (move['down'], [move['left'], move['down']])
}

for i in range(1, n + 1):
    for j in range(1, n + 1):
        signal = list(map(int, sys.stdin.readline().split()))
        signals[i][j] = signal

answer = set()
def bfs():
    q = deque()
    q.append(((1, 1), (-1, 0), 0))

    while q:
        now, prev_move, now_time = q.popleft()
        answer.add((now[0], now[1]))
        now_signal = signals[now[0]][now[1]][now_time%4]
        move = traffic[now_signal]
        if prev_move != move[0]:
            continue
        for nx, ny in move[1]:
            dx, dy = now[0] + nx, now[1] + ny
            if 1 <= dx <= n and 1 <= dy <= n:
                if not check[dx][dy] and now_time < t:
                    q.append(((dx, dy), (nx, ny), now_time + 1))
        
bfs()
print(len(answer))