def solution(n):
    def hanoi(num, start, end):
        if num == 1:
            return [[start, end]]
        another = 0
        for i in range(1,4):
            if i != start and i != end:
                another = i
                break
        return hanoi(num-1, start, another) + [[start, end]] + hanoi(num-1, another, end)
    return hanoi(n, 1, 3)
    
    return answer