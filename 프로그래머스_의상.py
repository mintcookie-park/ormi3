from collections import Counter
from functools import reduce

def solution(clothes):
    # 1. 의상 종류별 Counter를 만든다.
    counter = Counter([type for clothe, type in clothes])

    # 2. 모든 종류의 count + 1을 누적하여 곱해준다
    answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) - 1
    return answer