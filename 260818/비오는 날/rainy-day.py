n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

weathers = [Weather(date[i], day[i], weather[i]) for i in range(n)]

rainy = [w for w in weathers if w.weather == "Rain"]
rainy = sorted(rainy, key=lambda x: x.date)

print(rainy[0].date, rainy[0].day, rainy[0].weather)
