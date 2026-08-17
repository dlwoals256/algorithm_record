n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if (i+1) % 2 != 0:
        tmp = sorted(arr[:i+1])
        print(tmp[i//2], end=" ")
