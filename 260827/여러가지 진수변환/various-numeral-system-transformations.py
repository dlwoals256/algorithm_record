N, B = map(int, input().split())

res = []

while True:
    if N < B:
        res.append(N)
        break
    res.append(N % B)
    N //= B

for e in res[::-1]:
    print(e, end="")
