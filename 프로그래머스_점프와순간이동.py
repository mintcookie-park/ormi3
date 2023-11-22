def solution(n):
    answer = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            answer += 1
            n -= 1
    return answer