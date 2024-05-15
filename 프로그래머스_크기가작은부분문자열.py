def solution(t, p):
    answer = 0
    p_len = len(p)
    t_len = len(t)
    for i in range(t_len-p_len+1):
        num = int(t[i:i+p_len])
        if num <= int(p):
            answer += 1
    return answer