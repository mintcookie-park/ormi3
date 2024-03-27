def solution(n):
    arr = [[0] * i for i in range(1, n+1)]  # 주어진 n에 따른 직각삼각형 생성
    dirs = [(1, 0), (0, 1), (-1, -1)]  # 방향 집합(아래, 오른쪽, 왼쪽위)
    turn = 0  # 방향을 돌려줄 지표
    y, x = 0, 0  # 시작 좌표
    i = 1
    end_num = sum(i for i in range(1, n+1))  # 직각삼각형 내부의 칸 수
    while i <= end_num:
        arr[y][x] = i
        i += 1
        dy, dx = dirs[turn]
        ny = y + dy
        nx = x + dx
        # 다음 칸이 0부터 n 범위 내에 위치하고 값이 0일 경우 y, x값 변경
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 0:
            y, x = ny, nx
        # 범위를 벗어나거나 값이 0이 아닐 경우 방향 변경
        else:
            turn = (turn + 1) % 3
            dy, dx = dirs[turn]
            y += dy
            x += dx
    ans = []
    for row in arr:
        for item in row:
            ans.append(item)
    return ans
