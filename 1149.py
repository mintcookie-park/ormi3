n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input(.split())))
               
for house in range(1,n):
    for i in range(3):
        if i == 0:
           arr[house][i] += min(arr[house-1][1], arr[house-1][2])
        elif i == 1:
           arr[house][i] += min(arr[house-1][0], arr[house-1][2])
        else:
           arr[house][i] += min(arr[house-1][0], arr[house-1][1])
               
print(min(arr[n-1]))