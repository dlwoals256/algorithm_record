strs = [input() for _ in range(10)]
t = input()

printed = False
for i in range(10):
    if strs[i][-1] == t:
        print(strs[i])
        printed = True
if not printed:
    print("None")