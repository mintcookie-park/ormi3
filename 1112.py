num, n = map(int, input().split())
positive = n < 0 or (n >= 0 and num >= 0)
if not positive: num *= -1
remain = []
while num:
    q, r = divmod(num, n)
    if r < 0:
        q += 1
        r -= n
    remain.append(r)
    num = q
result = ''.join(map(str, remain[::-1]))
if remain:
    print(result) if positive else print(f'-{result}')
else:
    print(0)