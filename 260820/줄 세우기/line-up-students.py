n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

class Student:
    def __init__(self, h, w, i):
        self.h = h
        self.w = w
        self.i = i

students = [Student(students[i][0], students[i][1], students[i][2]) for i in range(n)]

students = sorted(students, key=lambda x: (-x.h, -x.w, x.i))

for s in students:
    print(s.h, s.w, s.i)