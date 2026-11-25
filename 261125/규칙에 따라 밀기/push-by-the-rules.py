s = input()
q = input()
for i in range(len(q)):
    if q[i] == "L":
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]
print(s)