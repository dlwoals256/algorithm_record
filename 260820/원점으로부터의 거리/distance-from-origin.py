n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

class Distance:
    def __init__(self, idx, dis):
        self.idx = idx + 1
        self.dis = dis

distances = [Distance(points[i][0], abs(points[i][1][0]-0) + abs(points[i][1][1]-0)) for i in range(n)]

distances = sorted(distances, key=lambda x: (x.dis, x.idx))

for d in distances:
    print(d.idx)