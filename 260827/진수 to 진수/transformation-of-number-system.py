a, b = map(int, input().split())
n = input()
num = 0
res = []
n = list(n)

for e in n:
    num = num * a + int(e)

while True:
    if num < b:
        res.append(num)
        break
    res.append(num % b)
    num //= b

for e in res[::-1]:
    print(e, end="")
