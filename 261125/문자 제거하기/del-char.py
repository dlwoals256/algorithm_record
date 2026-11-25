s = list(input())

while True:
    if len(s) <= 1:
        break
    i = int(input())
    if i >= len(s):
        s.pop(-1)
    else:
        s.pop(i)
    print("".join(s))