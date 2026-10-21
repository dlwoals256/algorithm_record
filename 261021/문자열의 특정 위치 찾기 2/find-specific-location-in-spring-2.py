strs = ["apple", "banana", "grape", "blueberry", "orange"]
t = input()
cnt = 0

for s in strs:
    if s[2] == t or s[3] == t:
        print(s)
        cnt += 1

print(cnt)
