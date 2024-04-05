N = (int(input())//100)*100
F = int(input())

#1씩 더하면서 F로 나눠지는지 확인
for i in range(100):
    if N%F == 0:
        N = str(N)
        break
    N += 1
print(N[-2:])