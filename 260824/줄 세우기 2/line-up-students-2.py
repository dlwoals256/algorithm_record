n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

class Student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

students = [Student(students[i][0], students[i][1], students[i][2]) for i in range(n)]

students = sorted(students, key=lambda x: (x.h, -x.w))

for s in students:
    print(s.h, s.w, s.num)
