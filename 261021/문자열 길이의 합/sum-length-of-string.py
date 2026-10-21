n = int(input())

sum = 0
cnt = 0

for i in range(n):
    s = input()
    sum += len(s)
    cnt += 1 if s[0] == "a" else 0

print(sum, cnt)