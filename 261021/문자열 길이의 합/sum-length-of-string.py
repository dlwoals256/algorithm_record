n = int(input())

strs = [input() for _ in range(n)]

sum = sum([len(s) for s in strs])
cnt = len([s for s in strs if s[0] == "a"])

print(sum, cnt)