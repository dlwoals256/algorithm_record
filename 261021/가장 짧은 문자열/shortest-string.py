a = input()
b = input()
c = input()

len_max = max([len(a), len(b), len(c)])
len_min = min([len(a), len(b), len(c)])

print(len_max - len_min)