m1, d1, m2, d2 = map(int, input().split())
A = input()

days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_day = 0
end_day = 0

for i in range(1, m1):
    start_day += days[i]
start_day += d1

for i in range(1, m2):
    end_day += days[i]
end_day += d2

weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
cnt = {weeks[k]: 0 for k in range(7)}

diff = end_day - start_day + 1

for i in range(diff):
    cnt[weeks[i % 7]] += 1

print(cnt[A])