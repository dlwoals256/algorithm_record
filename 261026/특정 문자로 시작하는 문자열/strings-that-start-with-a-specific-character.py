n = int(input())
strs = [input() for _ in range(n)]
t = input()

cnt = 0
sum = 0.0

for s in strs:
    if s[0] == t:
        cnt += 1
        sum += len(s)

print(cnt, f"{(sum / cnt):.2f}")