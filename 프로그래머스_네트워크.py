from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
    
    return answer

def BFS(n, computers, com, visited):
    visited[com] = True     # 방문을 했으므로 방문여부를 참으로 변경
    queue = deque()
    queue.append(com)
    
    for i in range(n):
        if visited[i] == False and computers[i][com] == 1 and i!=com:
            BFS(n, computers, i, visited)