n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

class Student:
    def __init__(self, name, sc1, sc2, sc3):
        self.name = name
        self.sc1 = sc1
        self.sc2 = sc2
        self.sc3 = sc3

students = [Student(name[i], score1[i], score2[i], score3[i]) for i in range(n)]

students = sorted(students, key=lambda x: x.sc1 + x.sc2 + x.sc3)

for s in students:
    print(s.name, s.sc1, s.sc2, s.sc3)
