N, B = map(int, input().split())

res = []

while True:
    if B == 4:
        if N < 4:
            res.append(N)
            break
        res.append(N % 4)
        N //= 4
    else:
        if N < 8:
            res.append(N)
            break
        res.append(N % 8)
        N //= 8

for e in res[::-1]:
    print(e, end="")
