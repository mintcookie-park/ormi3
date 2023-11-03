import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
# 돌의 계수 리스트
result = [1] * n

for i in range(1, n):
    # 돌의 계수를 비교할 변수 초기화
    result_max = 0
    for j in range(i):

        # 다음 밟을 돌의 높이와 그전에 있는 모든 돌의 높이 비교
        if a[i] > a[j]:
            # 돌의 계수 비교
            if result_max < result[j]:
                result_max = result[j]

    # 돌의 계수 카운트
    result[i] = result_max + 1

# 리스트에서 제일 큰 수를 출력
print(max(result))