n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

lines = [0] * 200

for i in range(n):
    for j in range(segments[i][0], segments[i][1]):
        lines[j] += 1

print(max(lines))
