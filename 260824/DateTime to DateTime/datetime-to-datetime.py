a, b, c = map(int, input().split())

if a < 11 or a <= 11 and b < 11 or a <= 11 and b <= 11 and c < 11:
    print(-1)
else:
    start = 11 * 24 * 60 + 11 * 60 + 11
    res = 0

    res += a * 24 * 60
    res += b * 60
    res += c

    print(res - start)
