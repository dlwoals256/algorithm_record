s = input()

ee = 0
eb = 0

if len(s) < 3:
    ee = s.count("ee")
    eb = s.count("eb")
else:
    for i in range(len(s)):
        if "ee" in s[i:i+2]:
            ee += 1
        if "eb" in s[i:i+2]:
            eb += 1

print(ee, eb)