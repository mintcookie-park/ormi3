def solution(s):
    answer = 0
    for c in s:
        if c == "(":
            answer += 1
        else:
            if answer > 0:
                answer -= 1
            else:
                return False
    if answer > 0:
        return False
    return True