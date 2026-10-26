strs = [input() for _ in range(10)]
t = input()

printed = False
for s in strs:
    if s[-1] == t:
        print(s)
        printed = True
if not printed:
    print("None")