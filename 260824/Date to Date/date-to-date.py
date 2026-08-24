m1, d1, m2, d2 = map(int, input().split())

start = 0
end = 0
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, m1):
    start += days[i]
start += d1

for i in range(1, m2):
    end += days[i]
end += d2

print(end - start + 1)
