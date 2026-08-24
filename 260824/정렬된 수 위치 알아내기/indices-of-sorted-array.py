n = int(input())
sequence = list(map(int, input().split()))

class Element:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val
        self.is_checked = False

sequence_res = [Element(i, sequence[i]) for i in range(n)]

temp_res = sorted(sequence_res, key=lambda x: (x.val, x.idx))

for i in range(n):
    for j in range(n):
        if  not sequence_res[i].is_checked and \
            sequence_res[i].val == temp_res[j].val and \
            sequence_res[i].idx == temp_res[j].idx:
            sequence_res[i].is_checked = True
            print(j+1, end=" ")
