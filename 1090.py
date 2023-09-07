arr = []
N = int(input())

for _ in range(N):
    arr.append(list(map(int, input().split())))

ans = [1 << 30] * (N + 1)  # 각 개수(인덱스)마다 최소거리를 저장하기 위해 아주큰값으로 초기화

for i in range(N):
    for j in range(N):
        mid_x, mid_y = arr[i][0], arr[j][1]  # 모든점의 좌표를 설정

        distance = []
        for h in range(N):  # 한점에서 부터 모든 점까지의 거리를 저장
            distance.append(abs(mid_x - arr[h][0]) + abs(mid_y - arr[h][1]))
        distance.sort()  # 최소 거리순으로 정렬
        sum_ = 0  # 각 거리마다 최소 거리를 저장
        for dist in range(N):
            sum_ += distance[dist]  # 각 좌표개수마다 거리를 더해준다.
            if ans[dist + 1] > sum_:  # 현재 거리에 저장된 최소거리보다 지금 구한 거리가 더 최소라면
                ans[dist + 1] = sum_  # 그값을 저장

print(*ans[1:])