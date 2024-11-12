def F(num):
    if num <= 2:
        return memo[num]
    # 중복 연산 막음 : 메모 활용
    elif memo[num] > 0:
        return memo[num]
    # 해시값 존재 안할 시 최소 한번은 연산해주어야 함.
    else :
        half = num //2
        if num % 2 == 0 :
            h0 = F(half)
            h1 = F(half-1)
            memo[num] = ((2*h1 + h0)*h0)%1000000007
            return memo[num]
        else : 
            h0 = F(half+1)
            h1 = F(half)
            memo[num] = (h0**2 + h1**2)%1000000007
            return memo[num]
            
## input
from collections import defaultdict
n = int(input())
memo = defaultdict(int)
memo[1],memo[2] = 1,1
## output
print(F(n))