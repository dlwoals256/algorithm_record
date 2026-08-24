m1, d1, m2, d2 = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_day = 0
end_day = 0

for i in range(1, m1):
    start_day += days[i]
start_day += d1

for i in range(1, m2):
    end_day += days[i]
end_day += d2

weeks = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

diff = end_day - start_day + 1

print(weeks[diff % 7])