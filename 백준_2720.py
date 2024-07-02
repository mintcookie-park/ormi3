n = int(input())

for _ in  range(n):
    c = int(input())
    arr = []
    for i in [25, 10, 5, 1]:
        arr.append(c // i)
        c = c % i
    print(*arr)