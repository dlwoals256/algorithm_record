s = input()

ee = 0
eb = 0

if len(s) < 3:
    ee = s.count("ee")
    eb = s.count("eb")
else:
    for i in range(len(s)-1):
        if s[i] == "e" and s[i+1] == "e":
            ee += 1
        if s[i] == "e" and s[i+1] == "b":
            eb += 1

print(ee, eb)