import sys
n = int(sys.stdin.readline())
line = []
for i in range(n-1):
  line.append(list(map(int, sys.stdin.readline().split())))

finish = list(map(int, sys.stdin.readline().split()))

time_a = 0
time_b = 0
work_a = 0
work_b = 0

for i in range(n-1):
  if n == 1:
    break

  time_a = min(line[i][0] + work_a, line[i][1] + line[i][3] + work_b)
  time_b = min(line[i][1] + work_b, line[i][0] + line[i][2] + work_a)
  work_a = time_a
  work_b = time_b

time_a += finish[0]
time_b += finish[1]

print(min(time_a, time_b))