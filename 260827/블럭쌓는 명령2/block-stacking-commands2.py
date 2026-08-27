n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = [0 for _ in range(n + 1)]

for comm in range(k):
    i, j = commands[comm]
    while i <= j:
        arr[j] += 1
        j -= 1

print(max(arr))
