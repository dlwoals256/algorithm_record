n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

class Person:
    def __init__(self, name, addr, region):
        self.name = name
        self.addr = addr
        self.region = region

people = [Person(name[i], address[i], region[i]) for i in range(n)]

people = sorted(people, key=lambda x: x.name, reverse=True)

print("name", people[0].name)
print("addr", people[0].addr)
print("city", people[0].region)
