N = input()
N = list(N)
res = []

num = 0

for n in N:
    num = num * 2 + int(n)

num *= 17

while True:
    if num < 2:
        res.append(num)
        break
    res.append(num % 2)
    num //= 2

for e in res[::-1]:
    print(e, end="")
