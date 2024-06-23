def gradient(a, b): # 기울기 계산
    return (a[1] - b[1]) / (a[0] - b[0])
 
def solution(dots):
    p1, p2, p3, p4 = dots[:4]
 
    if gradient(p3, p1) == gradient(p4, p2) or gradient(p4, p3) == gradient(p2, p1):
        return 1
    else:
        return 0