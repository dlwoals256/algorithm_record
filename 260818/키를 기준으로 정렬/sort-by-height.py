n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = [Person(name[i], height[i], weight[i]) for i in range(n)]

people = sorted(people, key=lambda x: x.height)

for person in people:
    print(person.name, person.height, person.weight)