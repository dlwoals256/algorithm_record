n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

def find(string, target):
    for i, s in enumerate(target):
        if string[i] != s:
            return False
    return True

str = [s for s in str if find(s, t)]

str = sorted(str)

print(str[k-1])