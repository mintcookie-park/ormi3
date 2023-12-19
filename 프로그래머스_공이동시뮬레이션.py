def solution(n, m, x, y, queries):
    answer = 0
    # 공이 한번에 움직인다고 생각한다
    # 공의 범위를 사각형으로 두고 생각해보자
    # 역으로 생각한다
    queries.reverse()
    xMin, xMax, yMin, yMax = x, x, y, y
    # print(queries)
    for ty, dx in queries:
        # 원래 열감소니깐 여기서는 열증가로 계산
        if ty == 0:
            yMax += dx

            if yMax >= m:
                yMax = m - 1

            if yMin != 0:
                yMin += dx


        # 원래는 열증가니깐 여기서는 열감소로 계산
        elif ty == 1:
            yMin -= dx

            if yMin < 0:
                yMin = 0

            if yMax != m - 1:
                yMax -= dx

        # 원래는 행감소니깐 여기서는 행증가로 계산
        elif ty == 2:
            xMax += dx

            if xMax >= n:
                xMax = n - 1

            if xMin != 0:
                xMin += dx

        # 원래는 행 증가니깐 여기서는 행감소로 계산
        elif ty == 3:
            xMin -= dx

            if xMin - dx < 0:
                xMin = 0

            if xMax != n - 1:
                xMax -= dx

        # 범위를 벗어나는 케이스가 생긴다면 공이 없다
        # print(xMin,xMax,yMin,yMax)

        if xMin > n or xMax < 0 or yMin > m or yMax < 0:
            return 0
        else:
            answer = (xMax - xMin + 1) * (yMax - yMin + 1)

    return answer