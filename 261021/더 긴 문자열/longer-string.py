a, b = input().split()

if len(a) == len(b):
    print("same")
else:
    res = a if len(a) > len(b) else b
    print(res, len(res))