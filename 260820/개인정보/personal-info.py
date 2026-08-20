n = 5
name = []
height = []
weight = []

for _ in range(n):
    na, h, w = input().split()
    name.append(na)
    height.append(int(h))
    weight.append(float(w))

class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

people = [Person(name[i], height[i], weight[i]) for i in range(n)]

people = sorted(people, key=lambda x: x.name)

print("name")
for p in people:
    print(p.name, p.h, f"{p.w:.1f}")

people = sorted(people, key=lambda x: -x.h)

print()
print("height")
for p in people:
    print(p.name, p.h, f"{p.w:.1f}")
