a = input()
b = input()

cnt = 0
for i in range(len(a)):
    if b in a[i:i+2]:
        cnt += 1

print(cnt)